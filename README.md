### 📚 AI Research Assistant (RAG + OCR + FastAPI + Streamlit)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)

An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents, build a searchable knowledge base, and ask questions in natural language using Large Language Models (LLMs). The system combines semantic search, keyword search, OCR, conversation memory, and citation-based responses.

🚀 Live Demo
🌐 Streamlit App: Add your Streamlit URL
⚡ FastAPI (Swagger): Add your FastAPI URL
💻 GitHub Repository: Add your GitHub Repository URL

### 📌 Features

- 📄 Upload one or multiple PDF documents

- 🔍 Automatic text extraction using PyMuPDF

- 🖼 OCR support for scanned PDFs using Tesseract

- ✂ Intelligent document chunking

- 🧠 FAISS Vector Database

- 🔎 Hybrid Search (Semantic + BM25)

- 🤖 Llama 3 via Groq API

- 💬 Conversational Question Answering

- 📚 Source Citation (Document & Page Number)

- 📝 Chat Memory

- 💾 SQLite Database

- ⭐ User Feedback Collection

- ⚡ FastAPI Backend

- 🎨 Modern Streamlit Dashboard

- 🐳 Docker Support

- 🔄 Ready for CI/CD Deployment

- 🏗 Project Architecture

PDF Upload
      │
      ▼
Text Extraction (PyMuPDF)
      │
      ▼
OCR (Tesseract)
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Llama 3 (Groq)
      │
      ▼
Answer + Sources

### 🛠 Tech Stack

|   Category       |    Technologies        |
| ---------------- | ---------------------- |        
|  Language        |      Python 3.12       |
|                  |                        |        
|    LLM           |  Llama 3 via Groq API  |
|                  |                        |
|  Framework       |   FastAPI, Streamlit   |
|                  |                        |                        
|    RAG           |      LangChain         |
|                  |                        |
|  Embeddings      |  HuggingFace Sentence  |
|                  |     Transformers       |
|                  |                        |
|  Vector DB       |        FAISS           |
|                  |                        |
| Keyword Search   |        BM25            |
|                  |                        |
|  Reranker        |     CrossEncoder       |
|                  |                        |
| Document Parsing |       PyMuPDF          |
|                  |                        |
|  Monitoring      |     Logging + CSV      |
|                  |                        |
|  Deployment      |  Docker,Render,Railway |
|                  |                        |
| Version Control  |     Git & GitHub       |
 

### Project Structure 

                User
                  │
                  ▼
          Streamlit Frontend
                  │
                  ▼
            FastAPI Backend
                  │
                  ▼
          Conversation Memory
                  │
                  ▼
           Query Expansion
                  │
                  ▼
         Hybrid Search Engine
        ┌────────────┴─────────────┐
        ▼                              ▼
     FAISS Search             BM25 Search
        └────────────┬─────────────┘
                       ▼
            CrossEncoder Reranker
                       ▼
           Relevant Context Chunks
                       ▼
              Llama 3 (Groq API)
                       ▼
                Generated Answer
                       ▼
        Monitoring • Logging • Feedback                 
     
### 📂 Project Folder Structure
AI-Research-Assistant/
│
├── app.py
├── api.py
├── requirements.txt
├── packages.txt
├── Dockerfile
├── README.md
│
├── dashboard/
│   ├── home.py
│   ├── upload.py
│   ├── chatbot.py
│   └── feedback.py
│
├── src/
│   ├── rag_pipeline.py
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_db.py
│   ├── retriever.py
│   ├── ocr.py
│   ├── memory.py
│   ├── streamlit_upload.py
│   └── utils.py
│
├── database/
│   ├── database.py
│   ├── models.py
│   └── init_db.py
│
├── vectorstore/
├── data/uploads/
└── chat_history/

### Workflow

- Upload PDF(s)
- Extract text
- Split into chunks
- Generate embeddings
- Store embeddings in FAISS
- BM25 indexes keywords
- User asks a question
- Query Expansion improves the query
- FAISS + BM25 retrieve candidate chunks
- CrossEncoder reranks results
- Top context sent to Llama 3
- Answer returned with sources
- Conversation stored in memory
- Interaction logged
- Feedback stored
- Evaluation metrics generated

### Evaluation

- Context Precision
- Context Recall
- Faithfulness
- Answer Relevancy
- Response Time
- Retrieval Accuracy

### Monitoring

- Interaction logging
- Response latency
- Error logging
- Feedback collection
- Cached responses
-Performance statistics

### ⚙ Installation

git clone https://github.com/Dhritikamal191/AI-Research-Assistant.git

cd AI-Research-Assistant

pip install -r requirements.txt

Create a .env file:
GROQ_API_KEY=YOUR_GROQ_API_KEY

Initialize the database:
python -m database.init_db

Run Streamlit:
streamlit run app.py

Run FastAPI:
uvicorn api:app --reload

### 📖 How It Works

- Upload one or more PDF files.

- Extract text using PyMuPDF.

- Apply OCR for scanned pages.

- Split text into chunks.

- Generate embeddings.

- Store vectors in FAISS.

- Retrieve relevant chunks using Hybrid Search.

- Generate answers with Llama 3.

- Display document citations.

### 📊 Key Features

- Hybrid Retrieval

- OCR-enabled document processing

- Citation-based responses

- Conversation memory

- SQLite chat history

- User feedback system

- REST API support

- Multi-document retrieval

- Streamlit dashboard

### 📈 Future Enhancements

- User Authentication

- Multi-user Support

- PostgreSQL Integration

- Azure/OpenAI Support

- Document Summarization

- Speech-to-Text Queries

- Image Understanding

- Cloud Storage Integration

### 📸 Screenshots

Add screenshots of:
🏠 Home Page
📄 Upload Documents
💬 Chat Interface
📚 Source Citations
⭐ Feedback Page
⚡ FastAPI Swagger
🧪 API Endpoints
Method
Endpoint
Description
POST
/upload
Upload PDFs
POST
/build
Build Knowledge Base
POST
/chat
Ask Questions
GET
/history
Chat History
POST
/feedback
Submit Feedback

### 🤝 Contributing

Contributions are welcome!
Fork the repository.
Create a feature branch.
Commit your changes.
Push your branch.
Open a Pull Request.

### 📄 License

This project is licensed under the MIT License.

### 👨‍💻 Author

Dhritikamal Das
MSc MACS

Data Analytics & Machine Learning Enthusiast
Interested in NLP, LLMs, RAG Systems, and MLOps

⭐ If you found this project useful, consider giving it a Star on GitHub!
