🧠 RAG & Transformer Demo Project

This repository combines foundational research with practical demos for building Retrieval-Augmented Generation (RAG) applications using LangChain, Ollama, Groq, and OpenAI APIs. It includes interactive Streamlit apps, Jupyter notebooks, and reference materials.

📂 Repository Structure
├── attention.pdf          # Research paper: "Attention Is All You Need" (Transformer architecture)
├── ragstack.ipynb         # Notebook demo: RAG pipeline with LangChain + FAISS
├── simplerag.ipynb        # Minimal RAG example with LangChain
├── speech.txt             # Sample text file (freedom of speech content)
├── app.py                 # Streamlit app (Groq + FAISS retriever)
├── app.py (alt version)   # Streamlit app (OpenAI integration)
├── localama.py            # Streamlit app (Ollama local model integration)

📘 Files Overview
🔹 Research & Data

attention.pdf
The seminal paper introducing the Transformer architecture, which underpins modern LLMs such as GPT, BERT, and others
.

speech.txt
A sample text on freedom of speech
. Can be used for ingestion into RAG pipelines or testing embeddings.

🔹 Jupyter Notebooks

ragstack.ipynb
Full RAG pipeline demo:

Loads documents with LangChain loaders

Splits text into chunks

Embeds using Ollama embeddings

Stores in FAISS vector DB

Performs retrieval + question answering

simplerag.ipynb
A simplified RAG implementation showcasing the bare minimum to get document Q&A working.

🔹 Streamlit Applications

app.py (Groq version)

Uses Groq LLMs with LangChain

Retrieves context chunks via FAISS

Interactive Q&A interface with context display

app.py (OpenAI version)

Uses OpenAI models with LangChain

Simple Q&A chatbot interface

localama.py

Runs Ollama local models (e.g., Gemma)

Works offline if models are installed locally

Streamlit interface for Q&A

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/yourusername/rag-transformer-demo.git
cd rag-transformer-demo

2️⃣ Install Dependencies
pip install -r requirements.txt


(You’ll need langchain, streamlit, faiss, python-dotenv, ollama, etc.)

3️⃣ Environment Variables

Create a .env file with your keys:

OPENAI_API_KEY=your_openai_key
LANGCHAIN_API_KEY=your_langchain_key
GROQ_API_KEY=your_groq_key

4️⃣ Run Notebooks

Open Jupyter Lab/Notebook and try:

jupyter lab

5️⃣ Run Streamlit Apps
streamlit run app.py
streamlit run localama.py


Deploy chatbots with context retrieval using multiple LLM providers

Compare local (Ollama) vs cloud-hosted (Groq/OpenAI) models
