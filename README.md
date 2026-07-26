# 🎓 EduGenie – AI-Powered Personalized Learning Assistant

## 📌 Project Overview

EduGenie is an AI-powered personalized learning assistant developed using FastAPI and Generative AI technologies. The application provides intelligent learning support through question answering, concept explanation, quiz generation, text summarization, and personalized learning recommendations.

The project integrates Google Gemini API to generate educational responses and demonstrates how Generative AI can be used in educational applications to improve student learning experiences through interactive assistance.

---

# 🎯 Project Objectives

- Build an AI-powered educational assistant.
- Integrate Generative AI with FastAPI.
- Provide personalized educational support.
- Generate quizzes automatically.
- Explain complex concepts in simple language.
- Summarize educational content.
- Recommend personalized learning paths.
- Create a simple and interactive web interface.

---

# ✨ Features

## 1. Question Answering

Provides answers to educational questions using Generative AI.

## 2. Concept Explanation

Explains difficult topics in simple and understandable language.

## 3. Quiz Generation

Automatically generates multiple-choice questions based on user-selected topics.

## 4. Text Summarization

Converts lengthy educational content into short and meaningful summaries.

## 5. Learning Recommendations

Generates personalized learning roadmaps with beginner, intermediate, and advanced learning paths.

---

# 🛠 Technologies Used

- Python 3.x
- FastAPI
- Google Gemini API
- LaMini-Flan-T5 (Planned Integration)
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates
- Python Dotenv
- Uvicorn
- Prompt Engineering

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

## Clone Repository

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

Create a `.env` file:

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
5. Structured prompts are generated using prompt engineering techniques.
6. The request is processed using Generative AI models.
7. AI generates the educational response.
8. FastAPI returns the response.
9. The result is displayed through the web interface.

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
Module   Module   Module Module   Path Module

                   |
                   v

          Prompt Engineering

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

EduGenie processes user requests through FastAPI, selects the required educational module, applies structured prompts, communicates with the Generative AI model, and displays the generated response.

---

# 🧠 Prompt Engineering

EduGenie uses structured prompt engineering techniques to improve AI response quality.

Techniques used:

- Clear instruction-based prompts.
- Context-aware educational prompts.
- Topic-specific prompts.
- Structured response formatting.
- Learning-level based recommendations.

Prompt engineering helps generate accurate, relevant, and student-friendly responses.

---

# 🧪 Testing & Validation

EduGenie was tested locally to verify the functionality of different AI modules.

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
- User inputs were validated.
- AI responses were formatted properly.
- Application was successfully executed on a local server.

---

# 📸 Screenshots

## Home Page

<img width="1920" height="1080" alt="Home Page" src="https://github.com/user-attachments/assets/c03d88b0-38c4-4b3b-ba75-ead152c87efb" />


## Question Answering Output

<img width="1920" height="1080" alt="Question Answering" src="https://github.com/user-attachments/assets/11baadf0-c3ad-493c-8c74-f50ed4fe0207" />

<img width="1920" height="1080" alt="Question Answering Output" src="https://github.com/user-attachments/assets/62031e00-d9ea-4ef1-b836-d7013f08ff0c" />


## Concept Explanation Output

<img width="1920" height="1080" alt="Concept Explanation" src="https://github.com/user-attachments/assets/dc00eef9-c841-4852-9fec-5dc97dd03866" />


<img width="1806" height="998" alt="Screenshot 2026-07-26 202345" src="https://github.com/user-attachments/assets/cd29b798-bdb8-47e0-9283-400d5c5b7ed1" />


<img width="1822" height="997" alt="Screenshot 2026-07-26 202357" src="https://github.com/user-attachments/assets/c7df1fd1-b429-4850-a274-ebfb976f96cc" />


## Quiz Generation Output

<img width="1920" height="1080" alt="Quiz Generation" src="https://github.com/user-attachments/assets/693a1f8c-9945-41fc-b11a-8e64998f3655" />


## Summarization

<img width="1920" height="1080" alt="Screenshot 2026-07-25 104145" src="https://github.com/user-attachments/assets/31e4aa5d-faff-4c2b-819f-778bfe7f8350" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 104206" src="https://github.com/user-attachments/assets/be98d38a-d1f2-4054-91a1-6066c4265d8b" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 104216" src="https://github.com/user-attachments/assets/a1a4192d-615f-4732-b3a5-3b5eb9a781e2" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 104238" src="https://github.com/user-attachments/assets/566cb65b-2354-4ce6-9b76-591291443814" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 104251" src="https://github.com/user-attachments/assets/bf19c067-a81f-4b21-9f66-96ca539fce97" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 223024" src="https://github.com/user-attachments/assets/40aaf081-396d-4770-a8ae-f71ccd23718b" />



## Learning Path Recomendation
<img width="1920" height="1080" alt="Screenshot 2026-07-25 223106" src="https://github.com/user-attachments/assets/29b83c6f-d35a-4990-bf49-7949f8d2ab00" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 223116" src="https://github.com/user-attachments/assets/4b163558-ede2-4022-8884-ccaaf803de14" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 223125" src="https://github.com/user-attachments/assets/ff3398af-a3b3-4235-8786-a0eaa6e61583" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 223134" src="https://github.com/user-attachments/assets/1c2c3e76-fd19-41fc-be40-3a5a7594d5ba" />

<img width="1920" height="1080" alt="Screenshot 2026-07-25 223141" src="https://github.com/user-attachments/assets/3b7347f0-f56e-4892-b520-60a5341dae16" />

---

# 📸 Project Demo Video




# 📚 Future Enhancements

- LaMini-Flan-T5 complete integration.
- PDF Upload Support.
- Voice-based Learning Assistant.
- Student Login System.
- Progress Tracking Dashboard.
- Multi-language Support.
- PDF Notes Generation.
- Performance Analytics.

---

# 🗂️ ER Diagram / System Representation

EduGenie does not store user data in a database. The following representation shows the relationship between user input, AI requests, educational modules, Gemini API, and generated responses.

```
              +-------------+
              |    USER     |
              +-------------+
              | input_text  |
              +-------------+
                    |
                    v

              +-------------+
              | AI REQUEST  |
              +-------------+
              | module_type |
              | user_input  |
              +-------------+

                    |
 ------------------------------------------------
 |          |          |          |              |
 v          v          v          v              v

Q&A   Explanation    Quiz     Summary     Learning
Module   Module     Module    Module     Path Module


                    |
                    v

             +-------------+
             | GEMINI API  |
             +-------------+
             | AI Model    |
             +-------------+

                    |
                    v

             +-------------+
             | AI RESPONSE |
             +-------------+
             | response    |
             +-------------+
```

---

# 👨‍💻 Author

Project:
# 👨‍💻 Author

Submitted By:

Name: P Gayatri Satapathy 
Roll number: 324506402513

Branch: B.Tech CSE
College: Andhra University college of engineering 
Academic Year: 2024-2028
Technologies: Python | FastAPI | Google Gemini 1.5 Pro | LaMini-Flan-T5 | HTML | CSS | Jinja2
Internship: **APSCHE Skill Wallet Internship**


**EduGenie – AI Powered Personalized Learning Assistant**

---

# 📄 License

This project was developed for educational purposes as part of the **APSCHE Skill Wallet Internship Program**.
