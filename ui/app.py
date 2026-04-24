import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="PDF AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PDF AI Agent")
st.caption("Upload a PDF and chat with it in real time.")

# -----------------------------
# Session state
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

# -----------------------------
# Sidebar PDF upload
# -----------------------------

with st.sidebar:
    st.header("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:
        if st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        "application/pdf"
                    )
                }

                response = requests.post(
                    f"{API_URL}/upload-pdf",
                    files=files
                )

                if response.status_code == 200:
                    st.session_state.pdf_processed = True
                    st.session_state.messages = []
                    st.success("PDF processed successfully!")
                else:
                    st.error("PDF processing failed.")
                    st.write(response.text)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.success("Chat cleared.")

# -----------------------------
# Display existing chat messages
# -----------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

        if message["role"] == "assistant" and message.get("sources"):
            with st.expander("Sources"):
                for source in message["sources"]:
                    st.markdown(f"**{source['source']}**")
                    st.write(source["content"])

# -----------------------------
# Chat input
# -----------------------------

user_question = st.chat_input("Ask something about your PDF...")

if user_question:
    if not st.session_state.pdf_processed:
        st.warning("Please upload and process a PDF first.")
    else:
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_question
        })

        with st.chat_message("user"):
            st.write(user_question)

        # Call backend
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                payload = {
                    "session_id": "streamlit-chat-session",
                    "question": user_question
                }

                response = requests.post(
                    f"{API_URL}/ask",
                    json=payload
                )

                if response.status_code == 200:
                    data = response.json()

                    answer = data["answer"]
                    sources = data.get("sources", [])

                    st.write(answer)

                    if sources:
                        with st.expander("Sources"):
                            for source in sources:
                                st.markdown(f"**{source['source']}**")
                                st.write(source["content"])

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    })

                else:
                    error_msg = "Something went wrong while asking the agent."
                    st.error(error_msg)
                    st.write(response.text)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
# What it does?
"""
This creates your simple UI.
1. Upload PDF
2. Process it
3. Ask Question
4. See answer + sources
"""