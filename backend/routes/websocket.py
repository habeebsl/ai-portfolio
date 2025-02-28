import traceback
from dotenv import load_dotenv
from quart import Blueprint, current_app, websocket
from utils.redis_utils import RedisInterface
from utils.db_utils import VectorDatabase
from utils.model_utils import ChatMistral
from utils.constants import TTL

load_dotenv()

ws_api = Blueprint("ws_api", __name__, url_prefix="/api")

@ws_api.websocket("/ws")
async def ws():
    try:
        if not current_app.config.get("REDIS_CONNECTED", False):
            await websocket.close(1011, "Redis connection unavailable")
            return
        
        session_token = websocket.args.get("session_token")

        print(session_token)

        if not session_token:
            await websocket.send_json({"error": "Unauthorized"})
            return
        
        redis_client = current_app.config['REDIS_CLIENT']
        redis_interface = RedisInterface(redis_client, session_token, TTL)

        while True:
            data = await websocket.receive()
            
            if not data:
                break

            db = VectorDatabase(data)
            chat_mistral = ChatMistral()
            
            conversation_data = await redis_interface.get_conversations()
            conversation_data.append({"role": "user", "content": data})
            
            prompt_data = await db.get_prompt()
            assistant_response = ""

            async for chunk in chat_mistral.get_response(conversation_data, prompt_data):
                assistant_response += chunk
                await websocket.send(chunk)
            
            new_convos = [
                {"role": "user", "content": data},
                {"role": "assistant", "content": assistant_response}
            ]

            await redis_interface.save_conversations(new_convos)
            
            await websocket.send("__DONE__")

    except Exception as e:
        print(f"WebSocket error with full traceback: {traceback.format_exc()}")
    finally:
        await websocket.close(1000)