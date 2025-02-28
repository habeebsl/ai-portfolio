import os
from dotenv import load_dotenv
from mistralai import Mistral
from prompts.mistral_prompt import system_prompt

load_dotenv()

class ChatMistral:
    def __init__(self):
        self.model = "mistral-large-latest"
        self.client = Mistral(api_key=os.getenv("API_KEY"))

    async def get_response(self, conversation: list, data: str):
        messages = [
            {"role": "system", "content": system_prompt(data)},
            *conversation
        ]

        try:
            stream_response = self.client.chat.stream(
                model = self.model,
                messages = messages
            )

            for chunk in stream_response:
                yield chunk.data.choices[0].delta.content

        except Exception as e:
            print(f"Error getting response: {e}")
            yield f"Error: {str(e)}"