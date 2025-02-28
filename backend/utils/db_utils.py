import os
import asyncio
from functools import lru_cache
from typing import List
from concurrent.futures import ThreadPoolExecutor
from tenacity import retry, stop_after_attempt, wait_exponential
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_mistralai.embeddings import MistralAIEmbeddings
from prompts.info import documents

load_dotenv()


class VectorDatabase:
    _pc = None
    _embeddings = None
    _thread_pool = ThreadPoolExecutor(max_workers=4)
    
    index_data = {
        "personal_info": "personal: Personal and contact information for Habeeb Salami(Me), Professional goals, expertise areas, location.",
        "technical_skills": "skills: Technical skills including programming, frameworks, and AI expertise",
        "ai_therapist": "ai therapist: AI-powered therapy application using CBT principles",
        "keypoint": "keypoint: Text analysis and information extraction tool",
        "chattersort": "chattersort: AI chatbot conversation management extension", 
        "activity_builder": "activity builder: Interactive math learning game",
        "work_experience": "experience: Work history at Chattersort and Google DSC",
        "education": "education: Medical education at Igbinedion University",
        "projects": "projects: Overview of major software development projects"
    }

    def __init__(self, query: str):
        self.query = query
        self.index_name = "ai-portfolio"
        
        if VectorDatabase._pc is None:
            VectorDatabase._pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        if VectorDatabase._embeddings is None:
            VectorDatabase._embeddings = MistralAIEmbeddings(api_key=os.getenv("API_KEY"))
        
        self.pc = VectorDatabase._pc
        self.embeddings = VectorDatabase._embeddings
        self.pool = VectorDatabase._thread_pool
        self.vectorstore = None

        if not self.index_exists():
            self.initialize_pinecone_db()
            self.add_texts()

        self.vectorstore = PineconeVectorStore(
            index_name=self.index_name, embedding=self.embeddings
        )

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def index_exists(self) -> bool:
        """Checks if the Pinecone index already exists with retry mechanism."""
        return self.index_name in [index["name"] for index in self.pc.list_indexes()]

    def initialize_pinecone_db(self):
        """Creates a new Pinecone index if it doesn't exist."""
        self.pc.create_index(
            name=self.index_name,
            dimension=1024,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    def add_texts(self):
        """Indexes predefined text data into Pinecone in batches."""
        texts = list(self.index_data.values())
        batch_size = 100
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            PineconeVectorStore.from_texts(
                batch, index_name=self.index_name, embedding=self.embeddings
            )

    @lru_cache(maxsize=1000)
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def similarity_search(self, k: int = 5):
        """Performs cached similarity search with retry mechanism."""
        pinecone_results = self.vectorstore.similarity_search(self.query, k=k)
        return [doc.page_content for doc in pinecone_results]

    async def async_similarity_search(self, k: int = 5):
        """Asynchronous similarity search."""
        loop = asyncio.get_event_loop()
        results = await loop.run_in_executor(
            self.pool,
            self.similarity_search,
            k
        )
        return results

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def reranker(self, docs: List[str]):
        """Uses reranking with retry mechanism."""
        results = self.pc.inference.rerank(
            model="bge-reranker-v2-m3",
            query=self.query,
            documents=docs,
            top_n=2,
            return_documents=True,
        )
        return [data.document.text for data in results.data]

    async def async_reranker(self, docs: List[str]):
        """Asynchronous reranking."""
        loop = asyncio.get_event_loop()
        results = await loop.run_in_executor(
            self.pool,
            lambda: self.reranker(docs)
        )
        return results

    async def get_prompt_async(self) -> str:
        """Asynchronous version of get_prompt."""
        docs = await self.async_similarity_search()
        results = await self.async_reranker(docs)
        
        value_to_key = {v: k for k, v in self.index_data.items()}
        prompt = "\n\n".join(
            documents[value_to_key[text]] for text in results if text in value_to_key
        )
        return prompt

    async def get_prompt(self) -> str:
        """Synchronous version that runs the async method."""
        return await self.get_prompt_async()

    def __del__(self):
        """Cleanup resources properly."""
        if hasattr(self, 'vectorstore'):
            del self.vectorstore


if __name__ == "__main__":
    db = VectorDatabase("What roles do you specialize in")
    print(db.get_prompt())