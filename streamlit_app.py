import streamlit as st
import requests
import os

# Backend URL
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Vault", layout="wide")
st.title("📄 AI-Powered Vault Document System")
st.markdown("Upload your document and chat with it in natural language!")

# Sidebar for uploading document
st.sidebar.header("Upload Document")
uploaded_file = st.sidebar.file_uploader(
    "Choose a PDF or DOCX file", type=["pdf", "docx"]
)

if uploaded_file:
    # Save uploaded file locally
    save_path = os.path.join("data/uploads", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Send to backend for ingestion
    st.sidebar.info("Uploading and processing...")
    response = requests.post(
        f"{API_URL}/v1/upload",
        files={"file": open(save_path, "rb")}
    )

    if response.status_code == 200:
        st.sidebar.success("✅ Document uploaded and processed!")
    else:
        st.sidebar.error("❌ Upload failed!")

# Chat interface
st.subheader("Ask Questions About Your Document")
question = st.text_input("Type your question here:")

if st.button("Ask"):
    if not question:
        st.warning("Please enter a question.")
    else:
        # Make request to chat API
        payload = {"question": question}
        chat_resp = requests.post(f"{API_URL}/chat/ask", json=payload)
        if chat_resp.status_code == 200:
            data = chat_resp.json()
            answer = data.get("answer", "No answer found.")
            sources = data.get("sources", [])
            st.markdown(f"**Answer:** {answer}")
            if sources:
                st.markdown("**Sources:**")
                for src in sources:
                    st.markdown(f"- Document ID: {src['document_id']}, Score: {src['score']:.3f}")
        else:
            st.error(f"Error: {chat_resp.status_code}")
