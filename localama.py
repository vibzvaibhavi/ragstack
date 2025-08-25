# localama.py
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

load_dotenv()

MODEL_NAME = "gemma:latest"  # using your installed model

model = ChatOllama(model=MODEL_NAME, temperature=0.2)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("human", "{question}"),
    ]
)

chain = prompt | model | StrOutputParser()

st.title("LangChain Demo with Gemma (Ollama)")
input_text = st.text_input("Search the topic you want")

if input_text:
    with st.spinner("Thinking..."):
        try:
            answer = chain.invoke({"question": input_text})
            st.markdown("**Answer:**")
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")
