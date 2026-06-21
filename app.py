"""
Career Agent — main Streamlit app.

IMPORTANT: this file only handles what the user SEES and CLICKS.
All the real logic lives in modules/, so this file stays short and readable.

Run this with:  streamlit run app.py
"""

import streamlit as st
from modules.cv_reader import extract_cv_text

st.set_page_config(page_title="Career Agent", page_icon=":compass:", layout="wide")

st.title("Career Agent")
st.caption("Your CV, job-matched and interview-ready.")

# --- Shared state ---------------------------------------------------------
# Streamlit re-runs this entire script from top to bottom every time you
# click something. st.session_state is a dictionary that SURVIVES those
# re-runs, so we use it to remember the CV text once it's been extracted.
if "cv_text" not in st.session_state:
    st.session_state.cv_text = ""

# --- Tabs -------------------------------------------------------------
tab_cv, tab_job, tab_skills, tab_letter, tab_interview = st.tabs(
    ["CV", "Job description", "Skill gaps", "Cover letter", "Mock interview"]
)

with tab_cv:
    st.subheader("1. Upload your CV")
    uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

    if uploaded_file is not None:
        with st.spinner("Reading your CV..."):
            try:
                st.session_state.cv_text = extract_cv_text(uploaded_file)
                st.success("CV loaded successfully.")
            except Exception as e:
                st.error(f"Couldn't read this file: {e}")

    if st.session_state.cv_text:
        with st.expander("Preview extracted text"):
            st.text(st.session_state.cv_text)

with tab_job:
    st.subheader("2. Job description analysis")
    st.info("We'll build this in the next step.")

with tab_skills:
    st.subheader("3. Skill gap suggestions")
    st.info("Coming in a later step.")

with tab_letter:
    st.subheader("4. Cover letter generator")
    st.info("Coming in a later step.")

with tab_interview:
    st.subheader("5. Mock interview")
    st.info("Coming in a later step.")