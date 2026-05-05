import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("📄 AI Resume Analyzer")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (TXT only)", type=["txt"])

if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")

    chunks = resume_text.split("\n")
    embeddings = model.encode(chunks)

    st.success("Resume uploaded!")

    query = st.text_input("Ask about your resume")

    if query:
        q_emb = model.encode(query)
        scores = np.dot(embeddings, q_emb)
        context = chunks[np.argmax(scores)]

        prompt = f"""
        Based on this resume:
        {context}

        Question: {query}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write("🤖 Answer:")
        st.write(response.choices[0].message.content)