# 🎓 EduGenie – AI-Powered Personalized Learning Assistant

## 📌 Project Overview

EduGenie is an AI-powered educational assistant developed using FastAPI and Google Gemini API. The application provides personalized learning support by answering questions, explaining concepts, generating quizzes, summarizing educational content, and recommending learning paths based on the user's input.

The project demonstrates how Generative AI can be integrated into educational applications to improve learning experiences through intelligent and interactive assistance.

---

# 🎯 Project Objectives

- Build an AI-powered educational assistant.
- Integrate Google Gemini API with FastAPI.
- Provide personalized educational support.
- Generate quizzes automatically.
- Summarize long educational content.
- Recommend learning roadmaps for students.
- Create a simple and interactive web interface.

---

# ✨ Features

## 1. Question Answering

Provides accurate answers to educational questions using Google Gemini AI.

## 2. Concept Explanation

Explains difficult topics in simple language with clear understanding.

## 3. Quiz Generation

Automatically creates multiple-choice questions based on a selected topic.

## 4. Text Summarization

Converts lengthy educational content into short and easy-to-read summaries.

## 5. Learning Recommendations

Generates personalized learning roadmaps including beginner, intermediate, and advanced study resources.

---

# 🛠 Technologies Used

- Python 3.13
- FastAPI
- Google Gemini API
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates
- Python Dotenv
- Uvicorn

---

# 📂 Project Structure

```
EduGenie/

├── main.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# ⚙ Installation

## Clone the Repository

```bash
git clone <repository-url>
```

## Open Project Folder

```bash
cd EduGenie
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create Environment File

Create `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Run Application

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

# 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home Page |
| POST | /qa | Question Answering |
| POST | /explain | Concept Explanation |
| POST | /quiz | Quiz Generation |
| POST | /summarize | Text Summarization |
| POST | /learn/recommendations | Learning Recommendations |

---

# 🔄 Project Workflow

1. User enters educational input.
2. FastAPI receives the request.
3. Input validation is performed.
4. The required AI module is selected.
5. A structured prompt is sent to Google Gemini API.
6. Gemini generates the educational response.
7. FastAPI returns the response.
8. The result is displayed on the web interface.

---

# 🏗️ AI Workflow / Architecture

```
                User
                  |
                  |
        Educational Input
                  |
                  v
          FastAPI Backend
                  |
                  |
          Request Processing
                  |
                  v
        AI Module Selection
                  |
    --------------------------------
    |        |        |      |      |
    v        v        v      v      v

   Q&A  Explanation  Quiz  Summary  Learning
 Module   Module    Module Module  Path Module

                  |
                  v

          Google Gemini API

                  |
                  v

        AI Generated Response

                  |
                  v

          Web Interface Display
```

The system processes user requests through FastAPI, selects the required educational module, sends a structured prompt to Google Gemini, and displays the generated response to the student.

---

# 🧪 Testing & Validation

EduGenie was tested locally to verify the functionality of all AI modules.

## Test Cases

| Module | Test Input | Result |
|--------|------------|--------|
| Question Answering | "What is Artificial Intelligence?" | Successful response generated |
| Concept Explanation | "Explain Photosynthesis" | Structured explanation generated |
| Quiz Generation | "Generate quiz on Python Programming" | MCQ quiz generated |
| Text Summarization | "Summarize Machine Learning" | Summary generated |
| Learning Recommendation | "Roadmap for Web Development" | Learning path generated |

## Validation

- API endpoints were tested successfully.
- User inputs were validated before processing.
- AI responses were formatted for better readability.
- Application was successfully executed on a local server.

---

# 📸 Screenshots

screenshots of:

- Home Page
<img width="1920" height="1080" alt="Screenshot 2026-07-15 204955" src="https://github.com/user-attachments/assets/75d2ef6f-6cfd-4833-bb6f-debc4fea109f" />

-  Quiz Generation Output
<img width="1920" height="1080" alt="Screenshot 2026-07-15 202617" src="https://github.com/user-attachments/assets/e4e18a5c-fcd8-4023-af86-7f3582a49f2a" />

<img width="1920" height="1080" alt="Screenshot 2026-07-15 202537" src="https://github.com/user-attachments/assets/0f41e85d-d983-43a2-bb4d-31347f7a5686" />

- 
- Concept Explanation Output
- <img width="1920" height="1080" alt="Screenshot 2026-07-15 201152" src="https://github.com/user-attachments/assets/e87e09a9-a39b-4cc7-99e8-080dc12ccde8" />

<img width="1920" height="1080" alt="Screenshot 2026-07-15 201139" src="https://github.com/user-attachments/assets/2846ff9d-ab7e-4d01-a01f-af328a54a3a2" />



- Text Summarization Output
- <img width="1920" height="1080" alt="Screenshot 2026-07-15 202129" src="https://github.com/user-attachments/assets/a6d5858f-6124-464f-a436-3bb394d45008" />



---

# 📚 Future Enhancements

- PDF Upload Support
- Voice-based Learning Assistant
- Student Login System
- Progress Tracking Dashboard
- Multi-language Support
- PDF Notes Generation
- Performance Analytics

---

# 👨‍💻 Author
Submitted By: P Gayatri Satapathy 
Roll number: 324506492513
Harshini Kalakodimi
Roll Number: 324506402255
Branch: B.Tech CSE
College: Andhra University college of engineering 
Academic Year: 2024-2028
Technologies: Python | FastAPI | Google Gemini 1.5 Pro | LaMini-Flan-T5 | HTML | CSS | Jinja2
Internship: **APSCHE Skill Wallet Internship**

Project:
**EduGenie – AI Powered Personalized Learning Assistant**

# 🎓 EduGenie – AI-Powered Personalized Learning Assistant

## 📌 Project Overview

EduGenie is an AI-powered educational assistant developed using FastAPI and Google Gemini API. The application provides personalized learning support by answering questions, explaining concepts, generating quizzes, summarizing educational content, and recommending learning paths based on the user's input.

The project demonstrates how Generative AI can be integrated into educational applications to improve learning experiences through intelligent and interactive assistance.

---

# 🎯 Project Objectives

- Build an AI-powered educational assistant.
- Integrate Google Gemini API with FastAPI.
- Provide personalized educational support.
- Generate quizzes automatically.
- Summarize long educational content.
- Recommend learning roadmaps for students.
- Create a simple and interactive web interface.

---

# ✨ Features

## 1. Question Answering

Provides accurate answers to educational questions using Google Gemini AI.

## 2. Concept Explanation

Explains difficult topics in simple language with clear understanding.

## 3. Quiz Generation

Automatically creates multiple-choice questions based on a selected topic.

## 4. Text Summarization

Converts lengthy educational content into short and easy-to-read summaries.

## 5. Learning Recommendations

Generates personalized learning roadmaps including beginner, intermediate, and advanced study resources.

---

# 🛠 Technologies Used

- Python 3.13
- FastAPI
- Google Gemini API
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates
- Python Dotenv
- Uvicorn

---

# 📂 Project Structure

```
EduGenie/

├── main.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# ⚙ Installation

## Clone the Repository

```bash
git clone <repository-url>
```

## Open Project Folder

```bash
cd EduGenie
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create Environment File

Create `.env` file:

```env
GEMINI_API_KEY=_API_KEY
```

## Run Application

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

# 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home Page |
| POST | /qa | Question Answering |
| POST | /explain | Concept Explanation |
| POST | /quiz | Quiz Generation |
| POST | /summarize | Text Summarization |
| POST | /learn/recommendations | Learning Recommendations |

---

# 🔄 Project Workflow

1. User enters educational input.
2. FastAPI receives the request.
3. Input validation is performed.
4. The required AI module is selected.
5. A structured prompt is sent to Google Gemini API.
6. Gemini generates the educational response.
7. FastAPI returns the response.
8. The result is displayed on the web interface.

---

# 🏗️ AI Workflow / Architecture

```
                User
                  |
                  |
        Educational Input
                  |
                  v
          FastAPI Backend
                  |
                  |
          Request Processing
                  |
                  v
        AI Module Selection
                  |
    --------------------------------
    |        |        |      |      |
    v        v        v      v      v

   Q&A  Explanation  Quiz  Summary  Learning
 Module   Module    Module Module  Path Module

                  |
                  v

          Google Gemini API

                  |
                  v

        AI Generated Response

                  |
                  v

          Web Interface Display
```

The system processes user requests through FastAPI, selects the required educational module, sends a structured prompt to Google Gemini, and displays the generated response to the student.

---

# 🧪 Testing & Validation

EduGenie was tested locally to verify the functionality of all AI modules.

## Test Cases

| Module | Test Input | Result |
|--------|------------|--------|
| Question Answering | "What is Artificial Intelligence?" | Successful response generated |
| Concept Explanation | "Explain Photosynthesis" | Structured explanation generated |
| Quiz Generation | "Generate quiz on Python Programming" | MCQ quiz generated |
| Text Summarization | "Summarize Machine Learning" | Summary generated |
| Learning Recommendation | "Roadmap for Web Development" | Learning path generated |

## Validation

- API endpoints were tested successfully.
- User inputs were validated before processing.
- AI responses were formatted for better readability.
- Application was successfully executed on a local server.

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Question Answering Output
- Concept Explanation Output
- Quiz Generation Output
- Text Summarization Output
- Learning Recommendations Output

---

# 📚 Future Enhancements

- PDF Upload Support
- Voice-based Learning Assistant
- Student Login System
- Progress Tracking Dashboard
- Multi-language Support
- PDF Notes Generation
- Performance Analytics

---

# 👨‍💻 Author

Submitted By: P Gayatri Satapathy 
Roll number: 324506492513
Harshini Kalakodimi
Roll Number: 324506402255
Branch: B.Tech CSE
College: Andhra University college of engineering 
Academic Year: 2024-2028
Technologies: Python | FastAPI | Google Gemini 1.5 Pro | LaMini-Flan-T5 | HTML | CSS | Jinja2
Internship: **APSCHE Skill Wallet Internship**

Project:
**EduGenie – AI Powered Personalized Learning Assistant**

---

# 📄 License

This project was developed for educational purposes as part of the APSCHE Skill Wallet Internship Program.


---
# 🗂️ ER Diagram / System Representation

EduGenie does not store user data in a database. The following ER representation shows the relationship between users, AI requests, educational modules, Gemini API, and generated responses.

            +----------------+
            |     USER       |
            +----------------+
            | user_id        |
            | input_text     |
            +----------------+
                   |
                   |
                   v

            +----------------+
            |  AI REQUEST    |
            +----------------+
            | request_id     |
            | module_type    |
            | user_input     |
            +----------------+
                   |
      ---------------------------------
      |        |        |       |      |
      v        v        v       v      v

   +------+ +-----------+ +------+ +---------+ +-------------+
   | Q&A  | |Explanation| | Quiz | |Summary | | Learning    |
   |Module| |  Module   | |Module| | Module | | Path Module |
   +------+ +-----------+ +------+ +---------+ +-------------+

                   |
                   v

          +----------------+
          | GEMINI AI API  |
          +----------------+
          | AI Model       |
          | Generated Data |
          +----------------+

                   |
                   v

          +----------------+
          | AI RESPONSE    |
          +----------------+
          | response_text  |
          +----------------+



---

Internship: **APSCHE Skill Wallet Internship**

Project:
**EduGenie – AI Powered Personalized Learning Assistant**

---

# 📄 License

This project was developed for educational purposes as part of the APSCHE Skill Wallet Internship Program.


---
# 🗂️ ER Diagram / System Representation

EduGenie does not store user data in a database. The following ER representation shows the relationship between users, AI requests, educational modules, Gemini API, and generated responses.

            +----------------+
            |     USER       |
            +----------------+
            | user_id        |
            | input_text     |
            +----------------+
                   |
                   |
                   v

            +----------------+
            |  AI REQUEST    |
            +----------------+
            | request_id     |
            | module_type    |
            | user_input     |
            +----------------+
                   |
      ---------------------------------
      |        |        |       |      |
      v        v        v       v      v

   +------+ +-----------+ +------+ +---------+ +-------------+
   | Q&A  | |Explanation| | Quiz | |Summary | | Learning    |
   |Module| |  Module   | |Module| | Module | | Path Module |
   +------+ +-----------+ +------+ +---------+ +-------------+

                   |
                   v

          +----------------+
          | GEMINI AI API  |
          +----------------+
          | AI Model       |
          | Generated Data |
          +----------------+

                   |
                   v

          +----------------+
          | AI RESPONSE    |
          +----------------+
          | response_text  |
          +----------------+



---
