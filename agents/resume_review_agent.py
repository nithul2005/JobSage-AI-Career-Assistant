import os
from dotenv import load_dotenv
load_dotenv()

from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ResumeReviewAgent:
    def review_resume(self, resume_text):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": f"Review this resume and give detailed feedback:\n{resume_text}"}
            ],
        )
        return response.choices[0].message.content
