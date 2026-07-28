### 📚 AI Research Assistant (RAG + OCR + FastAPI + Streamlit)

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

- Category
- Technologies
- Language
- Python
- LLM
- Llama 3 (Groq)
- Framework
- LangChain
- Vector Database
- FAISS
- OCR
- Tesseract OCR
- PDF Processing
- PyMuPDF
- Search
- BM25 + Semantic Search
- Backend
- FastAPI
- Frontend
- Streamlit
- Database
- SQLite
- Deployment
- Streamlit Cloud, Render
- Containerization
- Docker

### 📂 Project Structure
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
