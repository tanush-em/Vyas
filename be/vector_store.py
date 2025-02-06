from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    vector_store = FAISS.from_texts(chunks, embeddings)
    vector_store.save_local("vyas_vectorstore")
    return vector_store