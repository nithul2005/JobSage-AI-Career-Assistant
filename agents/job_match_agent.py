from groq import Groq

client = Groq(api_key="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")

class JobMatchAgent:
    def find_matching_jobs(self, resume_text):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": f"Suggest relevant job roles for this resume:\n{resume_text}"}
            ],
        )
        return response.choices[0].message.content
