# 🎓 Aspire Code AI — Personalized Learning Recommendation System

> An AI-powered platform that analyzes student performance patterns and delivers personalized learning paths — bridging the gap in traditional one-size-fits-all education.

---

## 📌 Table of Contents

- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---

## ❗ Problem Statement

Traditional education systems treat every student the same — regardless of their individual pace, strength, or learning gaps. This leads to:

- ❌ No personalized learning paths for students with varying skill levels
- ❌ Students getting stuck on difficult topics with zero adaptive guidance
- ❌ Inefficient learning progression due to rigid, linear curricula

---

## ✅ Solution Overview

**Aspire Code AI** is a rule-based + ML-ready recommendation engine that:

1. Ingests student performance data (quiz scores, attempts, time spent)
2. Computes derived metrics like **Mastery Score** and **Knowledge Gap Index**
3. Recommends the **next topic** or **targeted practice** based on performance thresholds
4. Delivers results through an interactive **Streamlit dashboard**

---

## 📁 Project Structure

```
aspire-code-ai/
│
├── app.py                  # Streamlit dashboard (main UI)
├── data_loader.py          # CSV ingestion & normalization
├── feature_engineering.py  # Mastery score & knowledge gap computation
├── recommender.py          # Core recommendation logic
├── index.html              # Static landing page
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🛠 Tech Stack

| Layer              | Technology                          |
|--------------------|--------------------------------------|
| Core Analytics     | Python, Pandas, NumPy               |
| AI / ML Models     | Scikit-learn, XGBoost, Random Forest |
| Visualization      | Matplotlib, Seaborn, Streamlit Charts|
| User Interface     | Streamlit Framework                  |
| Frontend Landing   | HTML, Tailwind CSS, Font Awesome     |

---

## ✨ Features

- **Student Profile Input** — Enter Student ID, current topic, quiz scores, time spent, and attempt count via sidebar
- **Mastery Scoring** — Weighted formula combining quiz score and attempt efficiency
- **Knowledge Gap Detection** — Flags weak topics automatically based on score thresholds
- **Personalized Recommendations** — Suggests next topic or targeted practice resources
- **Performance Trend Chart** — Visual history of score progression
- **Clean Metrics Table** — Displays Knowledge Gap Index, Learning Progress Rate, and Mastery Score

---

## ⚙️ How It Works

### 1. Data Loading & Cleaning (`data_loader.py`)
```python
df.dropna(inplace=True)
df['normalized_score'] = df['quiz_score'] / 100
```
Reads student CSV data, removes null records, and normalizes scores to a 0–1 range.

### 2. Feature Engineering (`feature_engineering.py`)
```python
df['mastery_score'] = (df['quiz_score'] * 0.7) + ((1 / df['attempts']) * 30)
df['knowledge_gap']  = 100 - df['quiz_score']
```
- **Mastery Score** — Weighs quiz performance (70%) + attempt efficiency (30%)
- **Knowledge Gap** — Inverse of quiz score; higher gap = more reinforcement needed

### 3. Recommendation Engine (`recommender.py`)

| Condition         | Action                                      |
|-------------------|----------------------------------------------|
| Quiz Score < 60%  | Recommend **targeted practice** on same topic |
| Quiz Score ≥ 60%  | Advance to **next topic** in the curriculum   |

### 4. Dashboard (`app.py`)
Interactive Streamlit UI with sidebar inputs, metric cards, and a line chart for score history.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/aspire-code-ai.git
cd aspire-code-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit dashboard
streamlit run app.py
```

### `requirements.txt`
```
streamlit
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
```

---

## 🖥 Usage

1. Open the Streamlit app in your browser (default: `http://localhost:8501`)
2. Enter the **Student ID** in the sidebar (e.g., `S101`)
3. Select the **Current Topic** (e.g., Recursion)
4. Input the **Quiz Score**, **Time Spent**, and **Number of Attempts**
5. Click **"Generate AI Recommendation"**
6. View the personalized recommendation, metrics table, and performance chart

---

## 📊 Sample Output

```
Student ID     : S204
Current Topic  : Recursion
Quiz Score     : 45%

─────────────────────────────────────────
  Knowledge Gap Index    : 55
  Learning Progress Rate : 15%
  Mastery Score          : 41.5

  Status      : ⚠️ Needs Reinforcement
  Recommended : Recursion Practice
  Resource    : Intermediate Recursion Problem Set
─────────────────────────────────────────
```

---

## 🔮 Future Enhancements

- [ ] Integrate real ML models (XGBoost classifier) trained on historical student data
- [ ] Add multi-subject support beyond programming topics
- [ ] Implement collaborative filtering for peer-based recommendations
- [ ] Connect to a database (SQLite / PostgreSQL) for persistent student records
- [ ] Export recommendation reports as PDF

---

## 👤 Author

**Vijay.M**  
Aspire Code AI — Personal Learning Project  
© 2024 Aspire Code AI