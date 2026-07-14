import google.generativeai as genai

model = genai.GenerativeModel("gemini-3.0-flash")


def generate_quiz(topic):
    prompt = f"""
You are EduGenie, an AI quiz generator for students.

Create a quiz on the following topic:

Topic:
{topic}

Generate 5 multiple-choice questions.

For each question provide:

1. Question
2. Option A
3. Option B
4. Option C
5. Option D
6. Correct Answer
7. Short Explanation of the answer

Rules:
- Make questions educational and student-friendly.
- Include a mix of easy and medium difficulty.
- Use clear formatting.
- Focus on understanding, not memorization.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"