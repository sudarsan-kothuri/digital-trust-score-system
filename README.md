# 🛡️ Digital Trust Score System  
### AI-Based Fake Profile & Identity Detection  
**Prakasam Police Hackathon 2026 – Mission Y4**

---

## 📌 Overview

Digital Trust Score System is an AI-powered web application that detects fake social media profiles, impersonation accounts, and suspicious or AI-generated profile images.

It generates a **Trust Score (0–100)** with clear explanations to help users and law enforcement identify risky accounts quickly.

---

## 🎯 Problem Statement

Social media platforms are widely affected by:
- Fake accounts
- Identity impersonation
- AI-generated profile images
- Online scams and fraud

Manual verification is slow and unreliable.  
This system provides **automated initial-level screening** using AI + rule-based logic.

---

## 🚀 Features

### 👤 Profile Risk Analysis
Input:
- Username
- Bio
- Followers & Following
- Account age

Output:
- Trust Score (0–100)
- Risk Level (Low / Medium / High)
- Explanation of risk factors

---

### 🖼️ Profile Image Analysis
- Upload profile image
- Detect suspicious or AI-generated images
- Confidence score output

---

### 🧾 Impersonation Detection
- Username similarity check
- Display name comparison
- Pattern detection (e.g. `_01`, `official`, `real`)

Output:
- Similarity percentage
- Impersonation warning

---

### 📊 Trust Score Engine
Combines all signals:
- Profile data
- Image analysis
- Username similarity
- Behavioral indicators

Final Output:
- 🟢 Trusted
- 🟡 Medium Risk
- 🔴 High Risk

---

### 🧑‍💻 Admin Dashboard
- View analyzed profiles
- Filter by risk level
- View detailed reasons
- Track flagged accounts

---

## 🏗️ Tech Stack

Frontend:
- HTML5
- CSS3
- Bootstrap
- JavaScript

Backend:
- Python (Flask)

AI / ML:
- OpenCV
- Scikit-learn (optional)
- Pretrained models (lightweight)

Database:
- SQLite

---

## ⚙️ System Workflow

User submits profile details + image  
↓  
Flask backend receives request  
↓  
Profile analysis module runs  
↓  
Image analysis module runs  
↓  
Impersonation detection runs  
↓  
Trust score engine calculates final score  
↓  
Result displayed with explanation  
↓  
Data stored in database  
↓  
Admin dashboard shows flagged profiles  

---

## 📂 Project Structure

hackathon-project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── uploads/
│
├── models/
│   ├── profile_analyzer.py
│   ├── image_model.py
│   ├── impersonation.py
│   ├── trust_score.py
│
├── database/
│   └── app.db
│
└── utils/
    └── helpers.py

---

## 🧠 Trust Score Logic

Weighted scoring system:

- Profile completeness → 20%
- Username risk → 25%
- Image authenticity → 25%
- Followers/following ratio → 15%
- Account age → 15%

Final Score = Weighted sum of all factors

---

## 💻 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/sudarsan-kothuri/digital-trust-score-system.git
cd digital-trust-score-system

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   

3. Install Dependencies
pip install -r requirements.txt

4. Run Application
python app.py

5. Open in Browser
http://127.0.0.1:5000/