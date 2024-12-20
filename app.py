import json
import secrets
from datetime import timedelta

import redis
from redis import Redis
from flask_session import Session

from flask import Flask, render_template, jsonify, session, request
from decouple import config

from model import get_response

app = Flask(__name__)

app.config['SECRET_KEY']= secrets.token_hex(24)
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'flask-session:'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)
app.config['SESSION_REDIS'] = Redis(host='localhost', port=6379)
Session(app)


def update_conversation(role, content):
    conversation = session.get("conversation", [])
    conversation.append({"role": role, "content": content})
    session["conversation"] = conversation
    session.modified = True

@app.route("/")
def homepage():
    if not "conversation" in session:
        session["conversation"] = []
    print(session["conversation"])
    return render_template("index.html", conversations=session["conversation"])


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