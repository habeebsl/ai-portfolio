import json
import commonmark
from redis.asyncio import Redis

class RedisInterface:
    def __init__(self, redis_client: Redis, session_token: str, ttl: int = 3600):
        self.conversation_id = f'session:{session_token}'
        self.client = redis_client
        self.ttl = ttl

    async def save_conversation(self, role: str, content: str):
        messages = await self.get_conversations()
        received_content = content
    
        if role == "assistant":
            received_content = commonmark.commonmark(content)
        messages.append({"role": role, "content": received_content})

        exists = await self.client.exists(self.conversation_id)
        await self.client.set(self.conversation_id, json.dumps(messages))
        if not exists:
            await self.client.expire(self.conversation_id, self.ttl)

    async def save_conversations(self, conversations: list):
        messages = await self.get_conversations()
        cleaned_convos = []
        for convo in conversations:
            role = convo.get("role")
            content = convo.get("content")
            if role == "assistant":
                content = commonmark.commonmark(content)
            cleaned_convos.append({"role": role, "content": content})
        
        messages.extend(cleaned_convos)

        exists = await self.client.exists(self.conversation_id)
        await self.client.set(self.conversation_id, json.dumps(messages))
        if not exists:
            await self.client.expire(self.conversation_id, self.ttl)

    async def get_conversations(self):
        messages = await self.client.get(self.conversation_id)
        return json.loads(messages) if messages else []
        
