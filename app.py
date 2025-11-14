import streamlit as st
import json

from extract_text import extract_text_from_resume
from parse_basic import extract_email, extract_phone, extract_skills
from skills_extract import SKILL_LIST
from matcher import match_jobs


st.title("Simple Resume Parser + Job Matcher (Version A)")

uploaded_file = st.file_uploader("Upload your resume (TXT file only)")

if uploaded_file:
    text = extract_text_from_resume(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(text[:500])

    email = extract_email(text)
    phone = extract_phone(text)

    st.subheader("Basic Information")
    st.write("📧 Email:", email)
    st.write("📞 Phone:", phone)

    found_skills = extract_skills(text, SKILL_LIST)

    st.subheader("Detected Skills")
    st.write(found_skills)

    # Load job data
    with open("jobs.json") as f:
        jobs = json.load(f)

    results = match_jobs(found_skills, jobs)

    st.subheader("Job Matching Results")
    for r in results:
        st.write(f"### {r['job_title']}")
        st.write("Matched skills:", r['skills_matched'])
        st.write("Match Score:", r['score'])
        st.write("---")
