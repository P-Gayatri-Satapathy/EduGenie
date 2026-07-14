# API Endpoints

## Home

Endpoint:

GET /

Purpose:

Displays the EduGenie home page.

---

## Question Answering

POST /qa

Input:

{
    "question":"What is AI?"
}

Output:

{
    "answer":"..."
}

---

## Concept Explanation

POST /explain

Input:

{
    "topic":"Machine Learning"
}

Output:

{
    "answer":"..."
}

---

## Quiz Generation

POST /quiz

Input:

{
    "topic":"Python"
}

Output:

{
    "answer":"Generated Quiz"
}

---

## Summarization

POST /summarize

Input:

{
    "text":"Long educational paragraph..."
}

Output:

{
    "answer":"Summary"
}

---

## Learning Recommendation

POST /learn/recommendations

Input:

{
    "topic":"SQL"
}

Output:

{
    "answer":"Learning Roadmap"
}