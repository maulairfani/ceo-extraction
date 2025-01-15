# Save AR JSON into pinecone DB

import json
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import os
import uuid
import glob
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()

class VectorDB:
    def __init__(self):
        self.index_name = "financial-statements"
        self.index = Pinecone(api_key=os.getenv("PINECONE_API_KEY")).Index(self.index_name)
        self.embedding = OpenAIEmbeddings(model="text-embedding-3-large", api_key=os.getenv("OPENAI_API_KEY"))
        self.vector_store = PineconeVectorStore(index=self.index, embedding=self.embedding)

    def add_items(self, json_path: str):
        docs, ids = self._load_docs(json_path)
        batch_size = 1
        _ids = []
        
        for i in tqdm(range(0, len(docs), batch_size)):
            try:
                batch_docs = docs[i:i + batch_size]
                batch_ids = ids[i:i + batch_size]
                _ids.extend(self.vector_store.add_documents(documents=batch_docs, ids=batch_ids))
            except Exception as e:
                print(f"Error adding items of {json_path} at index {i}: {e}")
        
        return _ids

    def _load_docs(self, json_path: str):
        with open(json_path, 'r') as f:
            data = json.load(f)
        basename = os.path.basename(json_path)[:-5]

        ids = []
        docs = []
        for doc in data:
            doc_id = str(uuid.uuid4())
            ids.append(doc_id)

            metadata = {
                "page": doc["metadata"]["page"],
                "company": basename
            }
            doc = Document(
                page_content=doc["page_content"],
                metadata=metadata
            )
            docs.append(doc)
        
        return docs, ids

files = glob.glob("data/AR_JSON/*.json")
files = [os.path.normpath(file) for file in files]
vectordb = VectorDB()
for file in files:
    print("Adding items from", file)
    vectordb.add_items(file)