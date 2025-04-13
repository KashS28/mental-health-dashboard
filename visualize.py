import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
import os

# Download English word list for filtering
nltk.download('words')
from nltk.corpus import words
english_vocab = set(w.lower() for w in words.words())

# === Load Sentiment Data ===
df = pd.read_csv("data/sentiment_tweets.csv")

# === Create outputs folder ===
os.makedirs("outputs", exist_ok=True)

# === 📊 Sentiment Distribution Bar Chart ===
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='sentiment', order=['Positive', 'Neutral', 'Negative'], palette='pastel')
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Tweet Count")
plt.tight_layout()
plt.savefig("outputs/sentiment_distribution.png")
plt.show()

# === ☁️ Word Cloud (Filtered) ===
text_combined = ' '.join(df['clean_text'].dropna())
filtered_words = ' '.join(word for word in text_combined.split() if word.lower() in english_vocab)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_words)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Valid English Words")
plt.tight_layout()
plt.savefig("outputs/cleaned_wordcloud.png")
plt.show()

# === 📅 Time-Based Sentiment Trend ===
if 'created_at' in df.columns:
    try:
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        df = df.dropna(subset=['created_at'])
        df.set_index('created_at', inplace=True)

        sentiment_trend = df.groupby([pd.Grouper(freq='D'), 'sentiment']).size().unstack(fill_value=0)

        plt.figure(figsize=(10, 5))
        sentiment_trend.plot(marker='o')
        plt.title("Sentiment Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Tweet Count")
        plt.tight_layout()
        plt.savefig("outputs/sentiment_over_time.png")
        plt.show()
    except Exception as e:
        print(f"⚠️ Could not generate time trend: {e}")
