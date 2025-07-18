# ui/streamlit_app.py

import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.job_match_agent import JobMatchAgent
from agents.interview_coach_agent import InterviewCoachAgent
from agents.resume_review_agent import ResumeReviewAgent
from utils.resume_processor import ResumeProcessor

# Streamlit Page Config
st.set_page_config(page_title="JobSage - AI Career Assistant", page_icon="🎯")

# App Title
st.title("🎯 JobSage - Your AI Career Assistant")

# Tabs for 3 Features
tabs = st.tabs(["Job Match Finder", "AI Interview Coach", "Resume Review Feedback"])

with tabs[0]:
    st.header("🔍 Job Match Finder")

    uploaded_file = st.file_uploader("Upload your Resume (PDF or TXT)", type=["txt", "pdf"], key="job_match")

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            resume_text = ""
            for page in reader.pages:
                resume_text += page.extract_text()
        else:
            resume_text = uploaded_file.read().decode("utf-8")

        if st.button("Find Matching Jobs"):
            processor = ResumeProcessor(resume_text)
            keywords = processor.extract_keywords()
            agent = JobMatchAgent()
            result = agent.find_matching_jobs(resume_text)
            st.success(result)

with tabs[1]:
    st.header("🤖 AI Interview Coach (Interactive Mock Interview)")

    interview_file = st.file_uploader("Upload your Resume (PDF or TXT)", type=["txt", "pdf"], key="interview_resume")

    role = st.text_input("What role are you applying for? (Optional, e.g., Data Scientist)")

    if interview_file is not None:
        if interview_file.type == "application/pdf":
            import PyPDF2
            reader = PyPDF2.PdfReader(interview_file)
            resume_text = ""
            for page in reader.pages:
                resume_text += page.extract_text()
        else:
            resume_text = interview_file.read().decode("utf-8")

        if st.button("Start Mock Interview - Ask Me a Question"):
            prompt = f"""Analyze this resume and the role '{role}' (if provided). 
Based on this, ask ONE relevant interview question only. 
Keep it clear and professional.
Resume:\n{resume_text}
"""
            agent = InterviewCoachAgent()
            question = agent.conduct_interview(prompt)
            st.session_state["current_question"] = question
            st.session_state["resume_text"] = resume_text
            st.session_state["role"] = role
            st.info(question)

        if "current_question" in st.session_state:
            user_answer = st.text_area("Your Answer:")

            if st.button("Submit My Answer for Feedback"):
                evaluation_prompt = f"""You are an AI interview coach.
Here is the question you asked: "{st.session_state['current_question']}"
Here is the candidate's answer: "{user_answer}"

Evaluate this answer critically. Provide:
1. Feedback: If it's good, say why. If bad, explain politely what's wrong.
2. Suggested Correct Answer (if their answer was wrong).
3. Encouragement and advice for improvement.

Resume: {st.session_state['resume_text']}
Role: {st.session_state['role']}
"""
                agent = InterviewCoachAgent()
                feedback = agent.conduct_interview(evaluation_prompt)
                st.success(feedback)


with tabs[2]:
    st.header("📝 Resume Review Feedback (For Your Dream Role)")

    review_file = st.file_uploader("Upload your Resume (PDF or TXT)", type=["txt", "pdf"], key="review_resume")

    target_role = st.text_input("What role are you applying for? (e.g., Data Scientist, Marketing Manager)")

    if review_file is not None:
        if review_file.type == "application/pdf":
            import PyPDF2
            reader = PyPDF2.PdfReader(review_file)
            resume_text = ""
            for page in reader.pages:
                resume_text += page.extract_text()
        else:
            resume_text = review_file.read().decode("utf-8")

        if st.button("Analyze My Resume"):
            prompt = f"""You are a professional career advisor AI.

Analyze this resume in detail for the role of '{target_role}'.

Provide feedback under these 3 clear headings:
1️⃣ Strengths: Skills, achievements, or sections that strengthen the candidate's suitability for this role.
2️⃣ Weaknesses: Gaps, weaknesses, poor phrasing, or areas where this resume may fail to impress for this role.
3️⃣ Suggestions for Improvement: Specific, practical tips to enhance this resume's chances of success when applying for '{target_role}'.

Be precise, clear, and professional.

Resume:\n{resume_text}
"""
            agent = ResumeReviewAgent()
            feedback = agent.review_resume(prompt)
            st.info(feedback)
