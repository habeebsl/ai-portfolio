import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from prompts.info import documents

load_dotenv()

class VectorDatabase:
    def __init__(self, query: str):
        self.query = query
        self.index_name = "ai-portfolio"
        
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
        self.vectorstore = None

        if not self.index_exists():
            self.initialize_pinecone_db()
            self.add_texts()

        self.vectorstore = PineconeVectorStore(
            index_name=self.index_name, embedding=self.embeddings
        )

    index_data = {
        "personal_info": "personal: Personal and contact information for Habeeb Salami(Me), Professional goals, expertise areas, location.",
        "technical_skills": "skills: Technical skills including programming, frameworks, and AI expertise",
        "ai_therapist": "ai therapist: AI-powered therapy application using CBT principles",
        "keypoint": "keypoint: Text analysis and information extraction tool",
        "chattersort": "chattersort: AI chatbot conversation management extension", 
        "activity_builder": "activity builder: Interactive math learning game",
        "ai_translator": "Multilingual translator with audio transcription and audio playback for translation",
        "work_experience": "experience: Work history at Chattersort and Google DSC",
        "education": "education: Medical education at Igbinedion University",
        "projects": "projects: Overview of major software development projects"
    }

    def index_exists(self) -> bool:
        """Checks if the Pinecone index already exists."""
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
        """Indexes predefined text data into Pinecone."""
        texts = list(self.index_data.values())
        PineconeVectorStore.from_texts(
            texts, index_name=self.index_name, embedding=self.embeddings
        )

    def similarity_search(self, k: int = 5):
        """Performs similarity search."""
        pinecone_results = self.vectorstore.similarity_search(self.query, k=k)
        return [doc.page_content for doc in pinecone_results]

    def reranker(self, docs: list):
        """Uses reranking."""
        results = self.pc.inference.rerank(
            model="bge-reranker-v2-m3",
            query=self.query,
            documents=docs,
            top_n=2,
            return_documents=True,
        )
        return [data.document.text for data in results.data]

    async def get_prompt(self) -> str:
        """Get prompt based on similarity search and reranking."""
        docs = self.similarity_search()
        results = self.reranker(docs)
        
        value_to_key = {v: k for k, v in self.index_data.items()}
        prompt = "\n\n".join(
            documents[value_to_key[text]] for text in results if text in value_to_key
        )
        return prompt

    def __del__(self):
        """Cleanup resources properly."""
        if hasattr(self, 'vectorstore'):
            del self.vectorstore


if __name__ == "__main__":
    db = VectorDatabase("What roles do you specialize in")
    print(db.get_prompt())