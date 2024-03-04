from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document, VectorStoreIndex, ServiceContext
from llama_index.core.indices.loading import load_index_from_storage
from llama_index.core.storage.storage_context import StorageContext
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ['OPENAI_API_KEY'] =OPENAI_API_KEY

def load_data():
    reader = SimpleDirectoryReader(input_dir="../data", recursive=True)
    docs = reader.load_data()
    index = VectorStoreIndex.from_documents(docs)
    return index

def persist_data(index, location = "../storage"):
    index.storage_context.persist(location)
    storage_context = StorageContext.from_defaults(persist_dir="../storage")
    return storage_context

def load_from_db():
    storage_context = StorageContext.from_defaults(persist_dir="../storage")
    index = load_index_from_storage(storage_context)
    return index
