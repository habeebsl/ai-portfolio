import os
import uuid
import random
from dotenv import load_dotenv
from quart import Blueprint, jsonify, request, current_app
from utils.redis_utils import RedisInterface
from utils.constants import PROMPTS, TTL

load_dotenv()

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/session/data")
async def get_session_data():
    try:
        if not current_app.config.get("REDIS_CONNECTED", False):
            return jsonify({"error": "Redis is unavailable"}), 500
        
        session_token = request.cookies.get("session_token")
        conversation_data = []
        if session_token:
            redis_client = current_app.config['REDIS_CLIENT']
            redis_interface = RedisInterface(redis_client, session_token, TTL)
            conversation_data = await redis_interface.get_conversations()
        random_prompts = random.sample(PROMPTS, 3)
        return jsonify({"conversations": conversation_data, "prompts": random_prompts})
    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred", 500

@api.route('/session/new', methods=['GET'])
async def create_new_session():
    secure=(os.getenv("SECURE", "false").lower() == "true")
    session_token = str(uuid.uuid4())

    response = jsonify({"message": session_token})
    response.set_cookie(
        "session_token",
        session_token,
        httponly=True,
        secure=secure,
        max_age=TTL,
        domain=os.getenv("FRONTEND_DOMAIN", None)
    )
    return response

@api.route('/session/validate', methods=['GET'])
async def validate_session():
    session_token = request.cookies.get("session_token")

    if not session_token:
        return jsonify({"error": "Unauthorized"})

    return jsonify({"message": session_token})

@api.route('/health', methods=['GET'])
async def health():
    return jsonify({"message": "Cronjob executed successfully"}), 200