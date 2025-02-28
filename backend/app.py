from functools import wraps
import os

from redis.asyncio import Redis
from quart import Quart, request, jsonify
from quart_cors import cors
from dotenv import load_dotenv
from routes.session import api
from routes.websocket import ws_api
from utils.config import ConfigSetup

load_dotenv()

def create_app():
    app = Quart(__name__)
    app = cors(
        app, 
        allow_origin=["http://localhost:5173", "http://127.0.0.1:5173"],
        allow_credentials=True
    )
    app.config.from_object(ConfigSetup)
    app.register_blueprint(api)
    app.register_blueprint(ws_api)

    return app

app = create_app()

@app.before_serving
async def setup():
    try:
        app.config['REDIS_CLIENT'] = Redis(
            host=ConfigSetup.REDIS_URL,
            port=ConfigSetup.REDIS_PORT,
            password=ConfigSetup.REDIS_PASSWORD,
            ssl=True
        )
        await app.config['REDIS_CLIENT'].ping()
        app.config["REDIS_CONNECTED"] = True
    except Exception as e:
        print(f"Redis connection error: {e}")
        app.config["REDIS_CONNECTED"] = False

if __name__ == "__main__":
    import asyncio
    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    config = Config()
    if os.getenv("SECURE", "false").lower() == "true":
        config.bind = ["0.0.0.0:8000"]
    else:
        config.bind = ["localhost:5000"]
    asyncio.run(serve(app, config))