import google.generativeai as genai

model = genai.GenerativeModel("gemini-3.0-flash")



def get_answer(question):
    try:

        prompt = f"""
You are EduGenie, an AI educational assistant.

Answer the student's question clearly and accurately.

Student Question:
{question}

Follow this format:

1. Definition / Direct Answer
2. Detailed Explanation
3. Real-Life Example
4. Key Points
5. Short Conclusion

Rules:
- Use simple language suitable for students.
- Use headings and bullet points.
- Explain step-by-step.
- Avoid unnecessary complex words.
- Make the answer useful for learning.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"