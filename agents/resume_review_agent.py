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
