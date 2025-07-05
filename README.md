# 💳 GPT-PayAudit – Smart Payment Anomaly Detector

GPT-PayAudit is an AI-powered web app that flags suspicious payment transactions using a combination of Machine Learning and GPT-4 explanations. It helps finance teams, auditors, or startups quickly detect duplicate charges, outliers, vendor fraud, and unusual spikes — all visualized in a beautiful dashboard with PDF export.

---

## 🚀 Features

- 📤 Upload any payment CSV
- 🧠 GPT-4 audit summary for flagged transactions
- ⚠️ ML-based anomaly detection (Isolation Forest)
- 📊 Interactive charts: Vendor-wise + Monthly spend
- 📄 Auto-generated PDF audit report
- 🖥️ Streamlit-based modern UI
- 🔐 Environment variables protected (.env ignored in Git)

---

## 💻 Tech Stack

| Layer       | Tech                              |
|-------------|-----------------------------------|
| Frontend    | Streamlit                         |
| Backend     | FastAPI                           |
| AI Engine   | OpenAI GPT-4                      |
| ML Model    | IsolationForest (scikit-learn)    |
| PDF Export  | ReportLab                         |
| Others      | Pandas, Requests, Python-dotenv   |

---

## 📦 How to Run Locally

### 🔧 Setup

```bash
git clone https://github.com/AayushA10/GPT-PayAudit-Smart-Payment-Anomaly-Detector.git
cd GPT-PayAudit-Smart-Payment-Anomaly-Detector

# Create virtualenv (optional)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

🔐 Set up your .env file
Create a .env file at the root:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

🧠 Run Backend
uvicorn backend.main:app --reload
# Visit: http://localhost:8000/docs (Swagger UI)

🖥️ Run Frontend (Streamlit)
streamlit run streamlit_app/Home.py
# Visit: http://localhost:8501

🧪 Sample Test CSV
Use the built-in file:
data/sample_transactions.csv

