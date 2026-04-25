# 🚀 AI Resume Analyzer

A smart web application that analyzes resumes and compares them with job descriptions to generate ATS scores, skill match percentage, and improvement suggestions.

---

## 🎯 Features

- Upload Resume (PDF)
- Extract and preview resume content
- Skill extraction from resume
- Job description matching
- ATS Score calculation
- Missing skills detection
- Interactive charts and visual insights

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- PyPDF2  

---

## ⚙️ How It Works

1. Upload your resume (PDF)  
2. Paste a job description  
3. Click Analyze Resume  
4. Get:
   - Skill Match %
   - ATS Score
   - Missing Skills
   - Charts

---
⚙️ Installation Steps
Follow these steps to set up and run the AI Resume Analyzer locally:

Make sure you have Python and Git installed.

1️⃣ Clone the Repository
git clone https://github.com/Altoks-AI/AI-Resume-Analyzer.git
cd FolderName
2️⃣ Set Up a Virtual Environment
python -m venv myenv
./myenv/Scripts/activate
3️⃣ Install Dependencies
Make sure you have pip updated, then install all required packages:

pip install -r requirements.txt
4️⃣ Set Up Your .env File
Create a .env file in the root directory and add your Groq API key from Groq

GROQ_API_KEY=your_groq_api_key_here
5️⃣ Run the Streamlit App
Launch the app locally using Streamlit:

streamlit run main.py
6️⃣ Open in Browser
Once the app starts, it will automatically open in your default web browser at:

http://localhost:8501
✅ Now you’re all set! Upload a resume, paste a job description, and let the AI analyze your resume for job-fit and provide suggestions.

Possible Changes you may want to make:
Change the prompt in main.py file to get the results in the way you want.
Embedding Model is "sentence-transformers/all-mpnet-base-v2" ,Change to the model you desire (Ex: BERT, SBERT,etc)
Currently using Groq API and LLM model is "llama-3.3-70b-versatile", Change is model is removed or use other API's like OpenAI-GPT-4o model.
Change the Title, Labels and other names and display formats according to your liking.
