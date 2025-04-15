# 🧠 Mental Health Sentiment Analysis Dashboard

A real-time data visualization dashboard that analyzes mental health-related conversations on Twitter using Natural Language Processing (NLP) and sentiment analysis.

---

## 📌 Overview

The **Mental Health Dashboard** is a dynamic visualization tool that tracks and displays public sentiment around mental health topics based on Twitter data. It empowers users to explore mental health trends, hashtags, and emotional context in real-time.

Built using:
- 🐍 Python
- 🧪 Tweepy (Twitter API v2)
- 🔍 VADER Sentiment Analysis
- 📊 Plotly, Matplotlib, Streamlit

---

## 🎯 Key Features

- 🔄 **Real-time Tweet Collection**  
  Fetches the latest tweets using the Twitter API based on user-defined hashtags.

- 💬 **Sentiment Analysis**  
  Classifies tweets as Positive, Negative, or Neutral using VADER.

- 📈 **Interactive Visualizations**  
  Line graphs, bar charts, and pie charts to visualize sentiment trends.

- 📝 **Tweet Summaries**  
  Short summaries highlighting the tone of public conversation.

- 🎯 **Hashtag Customization**  
  Users can choose and compare hashtags of interest.

---

## 🚀 Live Demo

🌐 [Click here to try the app](https://mental-health-dashboard-eece5642.streamlit.app/)

<!-- Optional: Add a screenshot or GIF of your dashboard -->
<!-- ![Dashboard Screenshot](demo.gif) -->

---

## 🛠️ Tech Stack

| Tool           | Purpose                                  |
|----------------|------------------------------------------|
| Python         | Core programming language                |
| Tweepy         | Collecting tweets using Twitter API      |
| VADER (NLTK)   | Sentiment analysis engine                |
| Pandas, NumPy  | Data manipulation and preprocessing      |
| Plotly, Matplotlib | Data visualization                 |
| Streamlit      | Web app framework                        |

---

## 📂 Project Structure

mental-health-dashboard/ 
├── api.py # Core API logic and tweet collection 
├── sentiment.py # Sentiment analysis functions 
├── app.py # Streamlit dashboard app 
├── requirements.txt # Dependencies 
└── README.md # Project documentation
