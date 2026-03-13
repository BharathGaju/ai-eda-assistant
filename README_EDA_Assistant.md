# 🤖 AI-Powered EDA Assistant

An intelligent web application that automatically analyzes any CSV dataset and generates insights, visualizations, and answers natural language questions — powered by LLM APIs.

---

## 🌐 Live Demo
👉 [Open Live App](https://bharathgaju-ai-eda-assistant.streamlit.app)

---

## 📌 Overview

Exploratory Data Analysis (EDA) is one of the most time-consuming steps in any data project. This app automates the entire process — upload a CSV file and instantly get statistical summaries, beautiful charts, and AI-generated insights in plain English.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📁 CSV Upload | Drag and drop any CSV file |
| 📋 Data Preview | View first 10 rows instantly |
| 📊 Basic Info | Rows, columns, and missing value count |
| 📈 Statistical Summary | Mean, median, std, min, max for all numeric columns |
| 🔍 Column Analysis | Data types and missing values per column |
| 📉 Distribution Plot | Interactive histogram for any column |
| 🔥 Correlation Heatmap | Visual correlation matrix between all numeric columns |
| 🧠 AI Insights | Auto-generated insights, patterns, anomalies, and suggestions |
| 💬 Ask AI Anything | Chat with AI about your specific dataset |

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** — Web application framework
- **Pandas** — Data manipulation and analysis
- **Matplotlib & Seaborn** — Data visualization
- **Groq API (LLaMA 3.3)** — AI insights generation
- **python-dotenv** — Environment variable management

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/BharathGaju/ai-eda-assistant.git
cd ai-eda-assistant
```

### 2. Install dependencies
```bash
pip install streamlit pandas matplotlib seaborn groq python-dotenv
```

### 3. Set up API key
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your-groq-api-key-here
```
Get your free API key at: https://console.groq.com/

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📂 Project Structure

```
ai-eda-assistant/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # API key (not committed to GitHub)
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```

---

## 💡 How It Works

```
User uploads CSV
      ↓
Pandas reads and processes the data
      ↓
App displays preview, stats, and charts
      ↓
Data summary sent to Groq LLM API
      ↓
AI generates insights in plain English
      ↓
User can ask follow-up questions
```

---

## 📸 Screenshots

### Data Preview & Basic Info
- Upload any CSV → instantly see rows, columns, missing values

### Visualizations
- Distribution histogram + Correlation heatmap side by side

### AI Insights
- Key insights, patterns, anomalies, and suggestions generated automatically

---

## 🎯 Use Cases

- **Data Analysts** — Speed up initial data exploration
- **Business Analysts** — Understand datasets without coding
- **Students** — Learn about datasets interactively
- **Data Scientists** — Quick sanity check on new datasets

---

## 📦 Requirements

```
streamlit
pandas
matplotlib
seaborn
groq
python-dotenv
```

---

## 👨‍💻 Author

**Bharath KG** — Data Analyst  
📧 bharath4637@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/bharath-k-g-2971a5bb)  
🐙 [GitHub](https://github.com/BharathGaju)

---

## ⭐ If you found this useful, please give it a star!
