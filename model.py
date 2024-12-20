import json
import markdown
from decouple import config
from mistralai import Mistral

api_key = config('API_KEY')
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def get_response(conversation):
    with open(r"prompts/response_prompt.txt", "r", encoding="utf-8") as file:
        intructions = file.read()
    messages = [
        {
            "role": "system",
            "content": intructions,
        }
    ]
    messages += conversation

    try:
        chat_response = client.chat.complete(
            model = model,
            messages = messages,
            response_format = {
                "type": "json_object",
            }
        )

        json_response = chat_response.choices[0].message.content
        print(json_response)
        parsed_json = json.loads(json_response)
        parsed_json["res"] = markdown.markdown(parsed_json["res"])
        return parsed_json
    except Exception as e:
        print(f"Error getting response: {e}")
        return None
    