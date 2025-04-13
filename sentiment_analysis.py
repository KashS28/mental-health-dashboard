import pandas as pd
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os

# Download VADER lexicon (only needs to run once)
nltk.download('vader_lexicon')

# === Load Twitter Data ===
df = pd.read_csv("data/twitter_mental_health_live.csv")

# === Clean the Tweets ===
def clean_text(text):
    text = str(text)
    text = re.sub(r"http\S+", "", text)         # Remove URLs
    text = re.sub(r"@\w+", "", text)            # Remove mentions
    text = re.sub(r"#", "", text)               # Remove hashtag symbol
    text = re.sub(r"\n", " ", text)             # Remove line breaks
    text = re.sub(r"[^\w\s]", "", text)         # Remove punctuation
    text = re.sub(r"\d+", "", text)             # Remove numbers
    text = text.lower()                         # Lowercase
    text = re.sub(r"\s+", " ", text).strip()    # Remove extra spaces
    return text

df["clean_text"] = df["text"].apply(clean_text)

# === VADER Sentiment Analysis ===
sia = SentimentIntensityAnalyzer()

df["compound"] = df["clean_text"].apply(lambda x: sia.polarity_scores(x)["compound"])

def get_sentiment_label(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["compound"].apply(get_sentiment_label)

# === Save the Sentiment-Annotated Tweets ===
os.makedirs("data", exist_ok=True)
df.to_csv("data/sentiment_tweets.csv", index=False)

print(f"✅ Sentiment analysis complete. {len(df)} tweets saved to 'data/sentiment_tweets.csv'")
