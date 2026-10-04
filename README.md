#RAG-Assistant.

RAG Enterprise Knowledge Assistant 🤖📚
An offline-capable, local Retrieval-Augmented Generation (RAG) enterprise knowledge assistant built using Python, Streamlit, LangChain, and ChromaDB. This system allows you to query your local documents securely without relying on external internet APIs for embeddings or generation after initial setup.
🚀 Features
100% Local & Offline Capable: Runs entirely on your local machine using HuggingFace sentence-transformers and ChromaDB.
Interactive Web UI: Powered by Streamlit for a clean, user-friendly chat and search interface.
Document Processing: Uses LangChain text splitters and document loaders to parse and chunk local knowledge bases.
Lightweight & Efficient: Optimized for limited data usage and rapid prototyping on Windows environments.
🛠️ Tech Stack
UI Framework: Streamlit  
Orchestration: LangChain  
Vector Database: ChromaDB  
Embeddings: sentence-transformers (all-MiniLM-L6-v2)
Language: Python (v3.14+)