import streamlit as st
import requests

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Clinical RAG AI Assistant",
    layout="wide"
)

# -----------------------------------
# Session State Initialization
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "active_pdf" not in st.session_state:
    st.session_state.active_pdf = None

# -----------------------------------
# Sidebar - PDF Upload
# -----------------------------------
with st.sidebar:
    st.header("📄 Document Upload")

    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

    if uploaded_file is not None:
        st.write(f"📎 {uploaded_file.name}")

        if st.button("Upload and Process PDF"):
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue())
            }

            response = requests.post(
                "http://localhost:8000/upload",
                files=files
            )

            if response.status_code == 200:
                st.success("✅ PDF uploaded and RAG pipeline initialized.")
                st.session_state.active_pdf = uploaded_file.name
            else:
                st.error("❌ Upload failed")

    if st.session_state.active_pdf:
        st.info(f"Active PDF: {st.session_state.active_pdf}")

# -----------------------------------
# Main Title
# -----------------------------------
st.title("🩺 Clinical RAG AI Assistant")

# -----------------------------------
# Display Chat History
# -----------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and "sources" in message:
            sources = message["sources"]

            if sources:
                with st.expander("📄 View Sources"):
                    for i, chunk in enumerate(sources, start=1):
                        st.markdown(f"**Chunk {i}:**")
                        st.markdown(chunk)
                        st.markdown("---")

# -----------------------------------
# Chat Input
# -----------------------------------
question = st.chat_input("Ask a medical question...")

if question:
    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Call FastAPI backend
    try:
        response = requests.post(
            "http://localhost:8000/query",
            json={"question": question}
        )

        if response.status_code == 200:
            data = response.json()
            answer = data.get("answer", "")
            sources = data.get("sources", [])

            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(answer)

                if sources:
                    with st.expander("📄 View Sources"):
                        for i, chunk in enumerate(sources, start=1):
                            st.markdown(f"**Chunk {i}:**")

                            # Highlight keywords
                            highlighted = chunk
                            keywords = question.lower().split()

                            for word in keywords:
                                if len(word) > 3:
                                    highlighted = highlighted.replace(
                                        word,
                                        f"**:orange[{word}]**"
                                    )

                            st.markdown(highlighted)
                            st.markdown("---")

            # Save assistant response
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources
            })

        else:
            st.error("❌ Backend error")

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")