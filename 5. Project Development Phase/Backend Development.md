# Backend Development

## Overview

The backend of EduGenie was developed using FastAPI, a modern and high-performance Python web framework. FastAPI manages user requests, processes educational queries, communicates with Google Gemini AI, and returns structured JSON responses to the frontend.

---

## Backend Components

- FastAPI
- Uvicorn Server
- REST API
- Google Gemini API
- Python Dotenv

---

## API Endpoints

| Method | Endpoint | Purpose |
|---------|----------|---------|
| GET | / | Home Page |
| POST | /qa | Question Answering |
| POST | /explain | Concept Explanation |
| POST | /quiz | Quiz Generation |
| POST | /summarize | Text Summarization |
| POST | /learn/recommendations | Learning Recommendations |

---

## Responsibilities

- Receive user requests.
- Validate input.
- Call the appropriate AI module.
- Generate AI responses.
- Return JSON output to the frontend.

---

## Benefits

- Fast processing
- Modular architecture
- Easy API integration
- High scalability