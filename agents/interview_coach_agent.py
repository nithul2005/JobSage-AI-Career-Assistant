import os
from dotenv import load_dotenv
load_dotenv()

from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class InterviewCoachAgent:
    def conduct_interview(self, user_input):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": f"Conduct a mock interview. Question: {user_input}"}
            ],
        )
        return response.choices[0].message.content
