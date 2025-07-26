from groq import Groq

client = Groq(api_key="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")

class InterviewCoachAgent:
    def conduct_interview(self, user_input):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": user_input}
            ],
        )
        return response.choices[0].message.content
