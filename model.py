import json
import markdown
from decouple import config
from mistralai import Mistral

api_key = config('API_KEY')
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def is_only_tabs(string):
    return all(char == '\t' for char in string)

def get_parsed_response(chat_response):
    count = 0
    for choice in chat_response:
        content = choice.message.content.strip()
        count += 1

        if is_only_tabs(content):
            print(f"choice {count} is only tabs")
            continue

        try:
            parsed_content = json.loads(content)
            if parsed_content == "" or parsed_content == {} or parsed_content == []:
                continue
            print(parsed_content)
            return parsed_content
        except json.JSONDecodeError:
            continue

    print("No valid JSON content found.")
    return None

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
            n=2,
            messages = messages,
            response_format = {
                "type": "json_object",
            }
        )

        json_response = chat_response.choices
        print(json_response)
        parsed_json = get_parsed_response(chat_response.choices)
        parsed_json["res"] = markdown.markdown(parsed_json["res"])
        return parsed_json
    except Exception as e:
        print(f"Error getting response: {e}")
        return None
    