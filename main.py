import streamlit as st
from PyPDF2 import PdfReader
import re
import pandas as pd

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("AI Resume Analyzer 🚀")
st.markdown("Upload resume + paste job description to get **ATS score, skill match, and suggestions**")


SKILLS = [
    "python", "java", "c++", "sql", "html", "css", "javascript",
    "machine learning", "data analysis", "pandas", "numpy",
    "react", "node", "mongodb", "git", "problem solving"
]


uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])


job_desc = st.text_area("Paste Job Description")

if uploaded_file:
    pdf = PdfReader(uploaded_file)
    text = ""

  
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    text_clean = re.sub(r"(?<!\n)\n(?!\n)", " ", text).lower()

    col1, col2 = st.columns([1, 1])

    
    with col1:
        st.subheader("Resume Preview")
        st.text_area("Text", value=text_clean, height=400)

   
    with col2:
        st.subheader("Analysis")

        if st.button("Analyze Resume"):

           
            found_skills = [skill for skill in SKILLS if skill in text_clean]
            jd_skills = [skill for skill in SKILLS if skill in job_desc.lower()]

            
            matched = list(set(found_skills) & set(jd_skills))
            missing = list(set(jd_skills) - set(found_skills))

            match_percent = int((len(matched) / len(jd_skills)) * 100) if jd_skills else 0

           
            ats_score = min(match_percent + 20, 100)

            st.success("Analysis Complete ✅")

            #
            st.subheader("🔍 Results")

            st.write(f"**Matched Skills:** {', '.join(matched) if matched else 'None'}")
            st.write(f"**Missing Skills:** {', '.join(missing) if missing else 'None'}")

            st.write(f"### Skill Match: {match_percent}%")
            st.progress(match_percent / 100)

            st.write(f"### ATS Score: {ats_score}/100")
            st.progress(ats_score / 100)

         
            df = pd.DataFrame({
                "Category": ["Matched", "Missing"],
                "Count": [len(matched), len(missing)]
            })

            st.subheader("Skill Comparison")
            st.bar_chart(df.set_index("Category"))

            
            st.subheader("Suggestions")
            if missing:
                st.write("• Add these skills to improve your resume:")
                for skill in missing:
                    st.write(f"- {skill}")
            else:
                st.write("Great! Your resume matches well with the job description.")
