from groq import Groq

client = Groq(api_key="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")

class ResumeReviewAgent:
    def review_resume(self, resume_text):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": f"Review this resume and give detailed feedback:\n{resume_text}"}
            ],
        )
        return response.choices[0].message.content
