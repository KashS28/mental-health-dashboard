

🧠 Mental Health Sentiment Analysis Dashboard
A real-time data visualization dashboard that analyzes mental health-related conversations on Twitter using Natural Language Processing (NLP) and sentiment analysis.

📌 Overview
The Mental Health Dashboard is a dynamic visualization tool that tracks and displays public sentiment around mental health topics based on Twitter data. It empowers users to explore mental health trends, hashtags, and emotional context in real-time.

Built using:

🐍 Python

🧪 Tweepy (Twitter API v2)

🔍 VADER Sentiment Analysis

📊 Plotly, Matplotlib, Streamlit

🎯 Key Features
🔄 Real-time Tweet Collection
Fetches the latest tweets using the Twitter API based on user-defined hashtags.

💬 Sentiment Analysis
Classifies tweets as Positive, Negative, or Neutral using VADER.

📈 Interactive Visualizations
Line graphs, bar charts, and pie charts to visualize sentiment trends.

📝 Tweet Summaries
Short summaries highlighting the tone of public conversation.

🎯 Hashtag Customization
Users can choose and compare hashtags of interest.

🚀 Demo
https://mental-health-dashboard-eece5642.streamlit.app/


🛠️ Tech Stack

Tool	Purpose
Python	Core programming language
Tweepy	Collecting tweets using Twitter API v2
VADER (NLTK)	Sentiment analysis
Pandas, NumPy	Data preprocessing
Plotly, Matplotlib	Data visualization
Streamlit	Web app interface
📂 Project Structure
bash
Copy
Edit
mental-health-dashboard/
├── api.py                # Core API logic and tweet collection
├── sentiment.py          # Sentiment analysis functions
├── app.py                # Streamlit dashboard app
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
⚙️ Setup Instructions
Clone the repo:

bash
Copy
Edit
git clone https://github.com/KashS28/mental-health-dashboard.git
cd mental-health-dashboard
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add Twitter API keys to your environment or directly in the api.py file.

Run the app:

bash
Copy
Edit
streamlit run app.py
🌍 Use Cases
Track how people feel about mental health-related events (e.g., awareness days, campaigns).

Analyze public sentiment for mental health organizations.

Understand emotional patterns over time for research or outreach.

🙋‍♀️ Author
Kashish Shah
Graduate Student @ Northeastern University
Specializing in Machine Learning & Data Visualization
LinkedIn | Portfolio (if any)
