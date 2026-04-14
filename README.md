# 🏥 Clinical RAG AI Assistant

A healthcare-focused Generative AI application that enables users to upload clinical documents (PDFs) and ask context-aware questions using Retrieval-Augmented Generation (RAG).

## 🚀 Features
- Upload and process clinical PDFs
- Extract and chunk text from documents
- Generate embeddings using OpenAI
- Store vectors using FAISS
- Retrieve relevant context
- Generate accurate answers using LLM
- Simple UI using Streamlit

## 🧠 Tech Stack
- Python
- FastAPI
- LangChain
- OpenAI
- FAISS
- Streamlit

## 📂 Project Structure
```
app/
 ├── api/
 ├── core/
data/
run.py
ui_app.py
```

## ⚙️ Setup Instructions

```bash
git clone <repo-link>
cd clinical-rag-ai-assistant
pip install -r requirements.txt
```

Create `.env` file:

```
OPENAI_API_KEY=your_api_key
```

Run backend:
```
python run.py
```

Run UI:
```
streamlit run ui_app.py
```

## 📌 Use Case
Designed for healthcare applications like:
- Clinical notes analysis
- Discharge summary Q&A
- Medical guideline search

## 🎯 Future Enhancements
- Pinecone integration
- Authentication system
- Deployment on AWS
- Advanced prompt tuning

---

## 💡 Author
Sai Keerthana