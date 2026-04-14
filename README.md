# 🔐 AI-Powered Threat Detection & Log Intelligence System

An AI-driven security log analyzer that detects suspicious login activity, classifies threats, and maps them to MITRE ATT&CK techniques. Built with FastAPI, Machine Learning, and deployed with Docker + Streamlit dashboard.

---

## 🚀 Features

- 🔍 Parses real-world SSH/auth logs
- 🤖 Detects anomalies using Isolation Forest (ML)
- ⚠️ Rule-based detection for brute-force & credential stuffing
- 🧠 Hybrid detection (ML + deterministic rules)
- 🗺️ MITRE ATT&CK mapping (T1110, T1110.004, T1036)
- 🌐 REST API with FastAPI
- 📊 Interactive dashboard using Streamlit
- 🐳 Fully containerized with Docker

---

## 🏗️ Architecture


---

## 🛠️ Tech Stack

- Python
- FastAPI
- Scikit-learn (Isolation Forest)
- Pandas
- Streamlit
- Docker

---


## ▶️ Run Locally

### 1. Clone repo
```bash
git clone <your-repo-url>
cd ai-security-log-analyzer
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train model
```bash
python train.py
```

### 5. Run API
```bash
uvicorn app.main:app --reload
```

### 6. Run dashboard
```bash
streamlit run dashboard.py
```

---

## 🐳 Run with Docker

### 1. Build image
```bash
docker build -t ai-security-analyzer .
```

### 2. Run container
```bash
docker run -p 8000:8000 -p 8501:8501 ai-security-analyzer
```

### 3. Access:
API: http://localhost:8000/docs

Dashboard: http://localhost:8501

---

## 🧪 Sample Output

{
  "ip": "192.168.1.10",

  "status": "suspicious",

  "reason": "Brute-force attempt detected",

  "severity": "high",

  "mitre_technique_id": "T1110",

  "mitre_technique_name": "Brute Force"

}

---

## 🧠 Key Learnings
- Designed hybrid AI + rule-based detection systems
- Implemented real-world log parsing and feature engineering
- Applied anomaly detection using Isolation Forest
- Integrated MITRE ATT&CK for standardized threat mapping
- Containerized full-stack AI application with Docker

