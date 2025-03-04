import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts.openai_prompt import system_prompt

load_dotenv()

class ChatOpenai:
    def __init__(self):
        self.model = "gpt-4o"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def get_response(self, conversation: list, data: str):
        messages = [
            {"role": "system", "content": system_prompt(data)},
            *conversation
        ]

        try:
            stream = self.client.chat.completions.create(
                model = self.model,
                messages = messages,
                stream=True,
            )

            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content

        except Exception as e:
            print(f"Error getting response: {e}")
            yield {"error": str(e)}