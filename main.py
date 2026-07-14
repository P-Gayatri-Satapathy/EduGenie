from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import google.generativeai as genai
import os

from qna import get_answer
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import learning_recommendations


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
print("Loaded API Key:", API_KEY[:10] + "..." if API_KEY else "No API Key")

genai.configure(api_key=API_KEY)


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Home page
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# Input validation function
def validate_input(value):
    if not value or value.strip() == "":
        return False
    return True


# Question Answering
@app.post("/qa")
async def qa(data: dict):

    question = data.get("question", "")

    if not validate_input(question):
        return JSONResponse(
            content={
                "status": "error",
                "message": "Please enter a question."
            }
        )

    try:
        answer = get_answer(question)

        return JSONResponse(
            content={
                "status": "success",
                "module": "Q&A",
                "answer": answer
            }
        )

    except Exception as e:
        return JSONResponse(
            content={
                "status": "error",
                "message": str(e)
            }
        )


# Explanation
@app.post("/explain")
async def explain(data: dict):

    topic = data.get("topic", "")

    if not validate_input(topic):
        return JSONResponse(
            content={
                "status": "error",
                "message": "Please enter a topic."
            }
        )

    return JSONResponse(
        content={
            "status": "success",
            "module": "Explanation",
            "answer": explain_topic(topic)
        }
    )


# Quiz
@app.post("/quiz")
async def quiz(data: dict):

    topic = data.get("topic", "")

    if not validate_input(topic):
        return JSONResponse(
            content={
                "status": "error",
                "message": "Please enter a quiz topic."
            }
        )

    return JSONResponse(
        content={
            "status": "success",
            "module": "Quiz",
            "answer": generate_quiz(topic)
        }
    )


# Summary
@app.post("/summarize")
async def summarize(data: dict):

    text = data.get("text", "")

    if not validate_input(text):
        return JSONResponse(
            content={
                "status": "error",
                "message": "Please enter text to summarize."
            }
        )

    return JSONResponse(
        content={
            "status": "success",
            "module": "Summary",
            "answer": summarize_text(text)
        }
    )


# Learning Recommendation
@app.post("/learn/recommendations")
async def learn(data: dict):

    topic = data.get("topic", "")

    if not validate_input(topic):
        return JSONResponse(
            content={
                "status": "error",
                "message": "Please enter a learning topic."
            }
        )

    return JSONResponse(
        content={
            "status": "success",
            "module": "Learning Recommendation",
            "answer": learning_recommendations(topic)
        }
    )