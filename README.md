# 🚀 AI Resume Analyzer

A smart **AI-powered web application** that evaluates resumes against job descriptions to generate **ATS scores, skill match insights, and personalized improvement suggestions**.

---

## 🎯 Key Features

* 📄 Upload and parse resumes (PDF format)
* 🔍 Extract and preview resume content
* 🧠 Intelligent skill extraction
* 🎯 Job description matching
* 📊 ATS score calculation
* ❌ Missing skills identification
* 📈 Interactive charts and visual insights
* 💡 Actionable suggestions for improvement

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Libraries:** Pandas, PyPDF2

---

## ⚙️ How It Works

1. Upload your resume (PDF)
2. Paste a job description
3. Click **Analyze Resume**
4. Get:

   * ✅ Skill Match Percentage
   * 📊 ATS Score
   * ❌ Missing Skills
   * 📈 Charts & Insights
   * 💡 Suggestions

---

## 💻 Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/yomkaX/ai-resume-analyzer.git
cd ai-resume-analyzer

---

### 2️⃣ Create Virtual Environment

python -m venv myenv

#### Activate:

Windows:
myenv\Scripts\activate

Mac/Linux:
source myenv/bin/activate

---

### 3️⃣ Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

---

### 4️⃣ Setup Environment Variables

Create a `.env` file and add:

GROQ_API_KEY=your_api_key_here

---

### 5️⃣ Run the App

streamlit run main.py

---

### 6️⃣ Open in Browser

http://localhost:8501

---

## ⚡ Customization

* Modify prompts in `main.py`
* Change embedding model (BERT / SBERT)
* Switch LLM (Groq / OpenAI)
* Update UI labels and layout

---

## 🚀 Future Improvements

* LinkedIn profile analysis
* AI resume rewriting
* Cover letter generator
* Multi-job comparison
* Advanced NLP scoring

---

## 🏁 Conclusion

This project demonstrates how **AI + NLP + Web Development** can be combined to build a practical tool that helps users **optimize resumes for better job opportunities**.

