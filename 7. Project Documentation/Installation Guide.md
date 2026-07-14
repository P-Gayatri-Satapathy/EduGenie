# Installation Guide

## Project Title

EduGenie – AI-Powered Personalized Learning Assistant

---

## Prerequisites

Before running the project, install the following:

- Python 3.10 or later
- Visual Studio Code
- Git
- Google Gemini API Key
- Internet Connection

---

## Required Python Packages

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install fastapi
pip install uvicorn
pip install google-generativeai
pip install python-dotenv
pip install jinja2
```

---

## Clone the Repository

```bash
git clone <repository-url>
cd EduGenie
```

---

## Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run the Project

```bash
uvicorn main:app --reload
```

---

## Open in Browser

```
http://127.0.0.1:8000
```

---

## Project Structure

- Backend (FastAPI)
- Frontend (HTML, CSS, JavaScript)
- AI Modules
- Templates
- Static Files
- Documentation

---

## Expected Output

The EduGenie web application opens successfully and provides AI-powered educational assistance through its available modules.