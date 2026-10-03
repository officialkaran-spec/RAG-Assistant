import os
import streamlit as st
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load local HuggingFace embedding model (Runs completely offline)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

st.title("🤖 RAG-Powered Enterprise Knowledge Assistant")
st.write(
    "Query your local enterprise documents (PDFs) securely and privately!"
)

# Ensure data folder exists
if not os.path.exists("data"):
  os.makedirs("data")

st.info(
    "💡 Tip: Place at least one PDF file inside the 'data' folder for the"
    " assistant to read."
)


# Function to load vector database
@st.cache_resource
def load_vector_db():
  loader = DirectoryLoader("data", glob="./*.pdf", loader_cls=PyPDFLoader)
  documents = loader.load()

  if not documents:
    return None

  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=500, chunk_overlap=50
  )
  texts = text_splitter.split_documents(documents)

  # Local ChromaDB Vector Store
  vectorstore = Chroma.from_documents(
      texts, embeddings, persist_directory="./chroma_db"
  )
  return vectorstore


db = load_vector_db()

if db is None:
  st.warning(
      "⚠️ No PDF files found in the 'data' folder. Please add a PDF file."
  )
else:
  st.success("✅ Database loaded successfully!")
  query = st.text_input("Ask a question from your documents:")
  if query:
    docs = db.similarity_search(query)
    st.subheader("Relevant Context / Answer:")
    for i, doc in enumerate(docs):
      st.write(f"**Result {i+1}:** {doc.page_content}")