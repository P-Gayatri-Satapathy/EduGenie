import google.generativeai as genai

model = genai.GenerativeModel("gemini-3.0-flash")


def learning_recommendations(topic):
    prompt = f"""
You are EduGenie, an AI career and learning guidance assistant.

Create a complete learning roadmap for:

Topic:
{topic}

Follow this structure:

1. Beginner Level
   - Basic concepts to learn
   - Required skills

2. Intermediate Level
   - Important topics
   - Practice activities

3. Advanced Level
   - Advanced concepts
   - Real-world applications

4. Projects to Practice
   - Beginner projects
   - Advanced projects

5. Recommended Resources
   - Books
   - Websites
   - YouTube channels

Rules:
- Make the roadmap suitable for students.
- Explain in a clear step-by-step order.
- Use headings and bullet points.
- Keep recommendations practical.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"