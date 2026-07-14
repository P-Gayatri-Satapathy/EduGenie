import google.generativeai as genai

model = genai.GenerativeModel("gemini-flash-latest")


def summarize_text(text):
    prompt = f"""
You are EduGenie, an AI educational summarizer.

Summarize the following content for students:

Content:
{text}

Follow this format:

1. Main Idea
2. Important Points
3. Key Terms
4. Short Explanation
5. Final Takeaway

Rules:
- Use simple language.
- Use bullet points.
- Keep the summary concise but complete.
- Highlight the most important information.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"