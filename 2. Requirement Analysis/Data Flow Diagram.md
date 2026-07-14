# Data Flow Diagram (DFD)

## Level 0 DFD

                +-----------------------+
                |       USER            |
                +-----------+-----------+
                            |
                            | Input Query
                            |
                            v
                +-----------------------+
                |    EduGenie System    |
                +-----------+-----------+
                            |
                            | AI Request
                            |
                            v
                +-----------------------+
                | Google Gemini API     |
                +-----------+-----------+
                            |
                            | AI Response
                            |
                            v
                +-----------------------+
                | Display Result        |
                +-----------------------+

## Data Flow

1. User enters a question or topic.
2. Frontend sends request to FastAPI.
3. FastAPI calls the corresponding AI module.
4. Gemini API generates the response.
5. FastAPI returns the response.
6. The result is displayed on the webpage.