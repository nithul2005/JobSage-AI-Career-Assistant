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
