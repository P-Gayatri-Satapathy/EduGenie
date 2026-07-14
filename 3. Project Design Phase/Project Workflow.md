# Project Workflow

## Step 1

The user opens the EduGenie web application.

↓

## Step 2

The user selects one of the available educational tasks.

- Question Answering
- Concept Explanation
- Quiz Generation
- Summarization
- Learning Recommendations

↓

## Step 3

The user enters a question, topic, or paragraph.

↓

## Step 4

The frontend sends the request to the FastAPI backend.

↓

## Step 5

The backend identifies the selected module.

↓

## Step 6

The module prepares a structured prompt and sends it to Google Gemini AI.

↓

## Step 7

Gemini generates an educational response.

↓

## Step 8

FastAPI receives the AI response.

↓

## Step 9

The response is formatted and returned as JSON.

↓

## Step 10

The frontend displays the generated educational content to the user.

---

## Workflow Summary

User
↓

Frontend (HTML/CSS)

↓

FastAPI Backend

↓

AI Module

↓

Google Gemini API

↓

Generated Response

↓

Frontend Displaynext
