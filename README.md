# DAO Workflow API

## 📌 Overview
This project is a Flask-based API that integrates MongoDB for storing DAO proposals and utilizes LangChain & LangGraph for analyzing governance insights. The API is built with Flask-RESTx and provides endpoints for retrieving and analyzing proposals.

## 🚀 Features
- Store and retrieve DAO proposals from MongoDB.
- Analyze proposals using an LLM (Groq API - Mixtral-8x7B).
- Modularized architecture for better scalability.
- Uses LangGraph to define a stateful workflow.
- Well-structured API with Flask-RESTx.

---

## 📂 Project Structure
```
/dao_workflow
│── .env                   # Environment variables
│── app.py                 # Main Flask application
│── config.py              # Configuration settings
│── database.py            # MongoDB connection
│── models.py              # Data models
│── workflow.py            # LangGraph workflow
│── services/
│   ├── llm_service.py     # LLM interactions
│   ├── dao_service.py     # DAO-related logic
│── routes/
│   ├── proposals.py       # Proposal API routes
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

---

## 🛠️ Installation
### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-repo.git
cd dao_workflow
```

### 2️⃣ Create a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables
Create a `.env` file and add the following:
```sh
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>
GROQ_API_KEY=your-groq-api-key
```

---

## 🔥 Running the Application
```sh
python app.py
```

### 📌 Available Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/proposals` | Fetch all DAO proposals |
| POST | `/api/analyze` | Analyze the first DAO proposal |

---


