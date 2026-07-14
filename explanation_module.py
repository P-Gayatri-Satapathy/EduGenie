import google.generativeai as genai

model = genai.GenerativeModel("gemini-3.0-flash")



def explain_topic(topic):
    prompt = f"""
You are EduGenie, an expert educational tutor.

Explain the following topic in simple language suitable for students.

Topic:
{topic}

Follow this structure:

1. Introduction
2. Definition
3. Detailed Explanation
4. How it Works / Process
5. Real-Life Examples
6. Advantages and Applications
7. Short Summary

Rules:
- Use simple words.
- Use headings and bullet points.
- Explain step-by-step.
- Make it easy for students to understand.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"