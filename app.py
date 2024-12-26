import random

import redis
from redis import Redis, RedisError
from flask_session import Session

from flask import Flask, render_template, jsonify, session, request
from decouple import config

from model import get_response

REDIS_URL = config('REDIS_URL')
REDIS_PORT = config('REDIS_PORT')
PASSWORD = config('REDIS_PASSWORD')

redis_client = redis.StrictRedis(
    host=REDIS_URL,
    port=REDIS_PORT,
    password=PASSWORD,
    ssl=True
)

app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'flask-session:'
app.config['SESSION_REDIS'] = redis_client
# Redis(host='localhost', port=6379)
Session(app)

prompts = [
    "Show me your best development work",
    "What technologies are you proficient in?",
    "Tell me about your work history and roles",
    "Show me a project you're most proud of",
    "What programming languages do you excel in?",
    "Can you provide an overview of your past projects and contributions?",
    "Share a coding challenge you’ve overcome successfully",
    "Which frameworks do you specialize in?",
    "How have your previous roles shaped your current skill set?",
    "What’s the most innovative feature you’ve implemented in a project?",
    "Do you have experience with cloud platforms? If so, which ones?",
    "What is a key lesson you’ve learned from your development experience?",
    "Give an example of a time you improved a system’s performance",
    "Which databases do you feel most comfortable working with?",
    "What are your most notable achievements in your development career?",
    "What’s the biggest project you’ve worked on to date?",
    "Tell me about a challenging bug you fixed and how you handled it.",
    "What’s your approach to staying up-to-date with new technologies?",
    "What development tools do you use regularly, and why?",
    "Show me an example of how you’ve optimized code or system architecture",
    "Which version control systems are you familiar with?",
    "What’s a key strategy you use to write clean and maintainable code?"
]


def update_conversation(role, content):
    try:
        conversation = session.get("conversation", [])
        conversation.append({"role": role, "content": content})
        session["conversation"] = conversation
        session.modified = True
        print(f"Updated conversation: {conversation}")
    except Exception as e:
        print(f"Error updating conversation: {str(e)}")

@app.route("/")
def homepage():
    try:
        # Verify Redis connection
        redis_client.ping()
        
        if "conversation" not in session:
            session["conversation"] = []
            session.modified = True
        
        random_prompts = random.sample(prompts, 3)
        return render_template("index.html", conversations=session["conversation"], prompts=random_prompts)
    except RedisError as e:
        print(f"Redis Error: {str(e)}")
        return "Redis connection failed", 500
    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred", 500


@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.json["message"]
    update_conversation("user", user_message)

    ai_response = get_response(session["conversation"])
    print(f"AI Response:\n{ai_response}")
    if ai_response.get("res", None):
        update_conversation("assistant", ai_response["res"])
        return jsonify({
            "message": ai_response["res"]
        })
    else:
        return jsonify({
            "error": "Something went wrong, please try again"
        })
    
        
if __name__ == "__main__":
    app.run(debug=config('DEBUG'))