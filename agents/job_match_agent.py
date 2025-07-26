from groq import Groq

client = Groq(api_key="ggsk_zt9InQpPDoxgNbc7mHprWGdyb3FYbqGY6vWlzcXKaGOVZsHu4bcD")

class JobMatchAgent:
    def find_matching_jobs(self, resume_text):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": f"Suggest relevant job roles for this resume:\n{resume_text}"}
            ],
        )
        return response.choices[0].message.content
