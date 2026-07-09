# 🎓 EduGenie - AI Powered Educational Assistant

EduGenie is an AI-powered educational assistant designed to make learning more interactive, accessible, and personalized. It enables students to ask academic questions, understand complex concepts, generate quizzes, summarize study material, and receive learning recommendations through an intuitive web interface.

The application is built using **FastAPI** for the backend, **Google Gemini AI** for intelligent content generation, and **HTML, CSS, JavaScript, and Jinja2** for the frontend. EduGenie provides a clean and responsive interface that helps learners improve their understanding efficiently.

---

## 🚀 Features

- 💡 AI-powered Question Answering
- 📚 Concept Explanation in simple language
- 📝 Automatic Quiz Generation
- 📄 Educational Text Summarization
- 🎯 Personalized Learning Recommendations
- 🌐 Responsive and User-Friendly Interface
- ⚡ FastAPI REST API Backend
- 🤖 Google Gemini AI Integration

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Uvicorn
- Python
- Pydantic

### AI & NLP
- Google Gemini API
- Prompt Engineering

### Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Development Tools
- VS Code
- Git & GitHub
- Python Virtual Environment

---

## 📂 Project Structure

```
EduGenie/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
│
├── models/
│   ├── request_models.py
│   └── response_models.py
│
├── routes/
│   ├── qa.py
│   ├── explain.py
│   ├── quiz.py
│   ├── summarize.py
│   └── recommend.py
│
├── services/
│   ├── gemini_service.py
│   └── prompts.py
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── utils/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/EduGenie.git
```

### 2. Navigate to the Project

```bash
cd EduGenie
```

### 3. Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Available Features

### Question Answering
Provides clear and accurate answers to academic questions.

### Concept Explanation
Explains difficult topics in a simple and easy-to-understand manner.

### Quiz Generation
Generates multiple-choice questions based on a selected topic.

### Text Summarization
Creates concise summaries from lengthy educational content.

### Learning Recommendations
Suggests the next topics to learn based on the user's current knowledge.

---

## 📸 Application Workflow

```
User
   │
   ▼
Frontend (HTML + CSS + JavaScript)
   │
   ▼
FastAPI Backend
   │
   ▼
Google Gemini AI
   │
   ▼
Processed Response
   │
   ▼
Displayed on Web Interface
```

---

## 📈 Future Enhancements

- User Authentication
- Chat History
- Dark Mode
- Voice-Based Learning
- PDF Upload and Summarization
- Notes Management
- Progress Tracking Dashboard
- Multi-language Support
- Learning Analytics
- Export Responses as PDF

---

## 🎯 Learning Outcomes

This project helped in understanding:

- FastAPI Development
- REST API Design
- Prompt Engineering
- Generative AI Integration
- Frontend Development
- Backend Architecture
- API Testing
- Full-Stack AI Application Development

---

## 👨‍💻 Author

**Kushal Konchada**

B.Tech - Computer Science and Engineering (Artificial Intelligence & Data Science)

Vishnu Institute of Technology

---

## 📄 License

This project is developed for educational and learning purposes.