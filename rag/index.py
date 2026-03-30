from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAI
from langchain_openai.embeddings.base import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

pdf_path = Path(__file__).parent / "nodejs.pdf"

# load this file in python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()


# print(docs[12])
# split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)


chunks = text_splitter.split_documents(documents=docs)

# Vector Embeddings
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
)


print("Indexing of documents above done")
