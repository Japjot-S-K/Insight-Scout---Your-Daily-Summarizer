import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import streamlit as st
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from transformers import pipeline

# Optional: for Lottie animations
from streamlit_lottie import st_lottie
import requests

# Load the local text2text generation model
@st.cache_resource
def load_teapot_pipeline():
    return pipeline("text2text-generation", model="teapotai/teapotllm")

teapot_pipe = load_teapot_pipeline()

# Helper: Load Lottie animation
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

# Lottie animation
lottie_news = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tljjah.json")

# Helper: Card-style output
def card(title, content):
    st.markdown(f"""
        <div style="background-color:#1e1e1e;padding:15px;border-radius:10px;
        margin-bottom:10px;border:1px solid #333;">
        <h4 style="color:#fff;">{title}</h4>
        <p style="color:#aaa;">{content}</p>
        </div>
    """, unsafe_allow_html=True)

# Main Title & Animation
st.markdown("<h1 style='text-align:center;'>🧠 Insight Scout</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: gray;'>Ask questions based on news URLs</p>", unsafe_allow_html=True)
st.divider()

if lottie_news:
    st_lottie(lottie_news, height=200, key="news")

# What's this app about button
with st.expander("📘 What's this app about?"):
    try:
        with open("README.md", "r", encoding="utf-8") as readme:
            st.markdown(readme.read())
    except FileNotFoundError:
        st.warning("README.md not found.")

# Layout: URL input on left, query box on right
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🌐 Enter your link here")
    url_1 = st.text_input("Enter your first link")
    url_2 = st.text_input("Enter your second link")
    url_3 = st.text_input("Enter your third link")
    process_url_clicked = st.button("Process URLs")
    urls = [u for u in [url_1, url_2, url_3] if u]

with col2:
    st.header("What's on your mind today?")
    query = st.text_input("e.g., What is the article about?")
    ask_button = st.button("🔍 Get Answer")

# Process URLs
if process_url_clicked and urls:
    try:
        st.info("🔎 Fetching content from URLs...")
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()

        st.success("✅ Content loaded successfully!")

        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(data)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.from_documents(docs, embeddings)

        st.session_state.vectorstore = vectorstore
        st.success("✅ Documents processed and stored in memory.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
elif process_url_clicked:
    st.warning("⚠️ Please enter at least one valid URL.")

# Answer the Question
if ask_button and query:
    if "vectorstore" in st.session_state:
        try:
            docs = st.session_state.vectorstore.similarity_search(query)
            combined_text = " ".join([doc.page_content for doc in docs])

            result = teapot_pipe(combined_text + " Question: " + query, max_length=512)
            response = result[0]['generated_text']

            card("🧠 Top Answer", response)
        except Exception as e:
            st.error(f"❌ Error generating answer: {e}")
    else:
        st.warning("⚠️ Please process URLs first.")

# Footer
st.markdown("---")
st.markdown("<center style='color: gray;'>Project by Japjot Singh Kashyap</center>", unsafe_allow_html=True)
