import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
import os
import subprocess

# === Page Config ===
st.set_page_config(page_title="Mental Health Sentiment Dashboard", layout="wide")

# === Load Resources ===
nltk.download('words')
from nltk.corpus import words
english_vocab = set(w.lower() for w in words.words())

# === Title and Header ===
st.title("🧠 Mental Health Sentiment Analysis Dashboard")
st.markdown("This dashboard analyzes real-time Twitter data related to mental health topics using NLP and data visualization.")

# === Refresh Tweets Button ===
if st.sidebar.button("🔁 Refresh Live Tweets"):
    with st.spinner("Fetching tweets from Twitter API..."):
        subprocess.run(["python3", "api.py"])
        subprocess.run(["python3", "sentiment_analysis.py"])
    st.success("Tweets refreshed! Please reload the app.")

# === Load Dataset ===
DATA_PATH = "data/sentiment_tweets.csv"
if not os.path.exists(DATA_PATH):
    st.error("Sentiment data not found. Please run 'sentiment_analysis.py' first.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# === Filters ===
st.sidebar.header("🔍 Filters")

# Sentiment filter
sentiments = df['sentiment'].unique().tolist()
selected_sentiments = st.sidebar.multiselect("Select sentiment(s):", sentiments, default=sentiments)
filtered_df = df[df['sentiment'].isin(selected_sentiments)]

# Keyword search
search_query = st.sidebar.text_input("Search for a keyword:")
if search_query:
    filtered_df = filtered_df[filtered_df['clean_text'].str.contains(search_query, case=False, na=False)]

# Tweet length slider
min_len, max_len = st.sidebar.slider("Tweet Length", 0, 300, (20, 280))
filtered_df = filtered_df[filtered_df['clean_text'].str.len().between(min_len, max_len)]

# === Summary Stats ===
st.markdown("### 🔢 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Tweets", len(filtered_df))
col2.metric("Avg Length", round(filtered_df['clean_text'].str.len().mean(), 1))
col3.metric("Positive %", f"{(filtered_df['sentiment'] == 'Positive').mean() * 100:.1f}%" if len(filtered_df) > 0 else "0%")

# === Sentiment Distribution Plot ===
st.subheader("📊 Sentiment Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x='sentiment', order=['Positive', 'Neutral', 'Negative'], palette='pastel', ax=ax1)
st.pyplot(fig1)

# === Word Cloud ===
st.subheader("☁️ Word Cloud (English words only)")
text = " ".join(filtered_df['clean_text'].dropna())
filtered_words = " ".join(word for word in text.split() if word.lower() in english_vocab)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_words)
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.imshow(wordcloud, interpolation='bilinear')
ax2.axis('off')
st.pyplot(fig2)

if 'created_at' in df.columns:
    st.subheader("📅 Sentiment Trend Over Time")
    try:
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        df = df.dropna(subset=['created_at'])
        df.set_index('created_at', inplace=True)
        trend_df = df.groupby([pd.Grouper(freq='D'), 'sentiment']).size().unstack(fill_value=0)

        fig3, ax3 = plt.subplots(figsize=(10, 4))
        trend_df.plot(marker='o', ax=ax3)
        plt.xlabel("Date")
        plt.ylabel("Tweet Count")
        plt.title("Sentiment Over Time")
        st.pyplot(fig3)
    except Exception as e:
        st.warning(f"Could not generate trend chart: {e}")

if st.checkbox("📄 Show Raw Tweet Data"):
    st.dataframe(filtered_df[['created_at', 'clean_text', 'sentiment']])

st.markdown("---")
st.caption("Built with 💙 by Kashish Shah & Gayathri Suresh | Northeastern University | EECE5642 - Data Visualization Final Project")
