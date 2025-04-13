import tweepy
import pandas as pd
import urllib.parse
import os


import time
time.sleep(15)


# === Twitter API Bearer Token ===
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHxN0gEAAAAAYmC7ziqTKiiNqcOlYfzY0HklfRM%3DSzv8CZnw9RGcCgxoRnr0miq3Yi92u27HPpGdwNr7U262wmxSDD"

# Decode token if it's URL encoded (starts with AAAAA...)
bearer_token = urllib.parse.unquote(bearer_token)

# Initialize Tweepy Client
client = tweepy.Client(bearer_token=bearer_token)

# === Search Query ===
query = "#mentalhealth OR #depression OR #anxiety -is:retweet lang:en"

# === Fetch Tweets ===
response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["id", "text", "created_at", "author_id", "lang"]
)

# === Extract Tweets ===
tweets = []
if response.data:
    for tweet in response.data:
        tweets.append({
            "tweet_id": tweet.id,
            "author_id": tweet.author_id,
            "created_at": tweet.created_at,
            "text": tweet.text
        })

# === Save to CSV ===
os.makedirs("data", exist_ok=True)
df = pd.DataFrame(tweets)
df.to_csv("data/twitter_mental_health_live.csv", index=False)

print(f"✅ Saved {len(df)} tweets to 'data/twitter_mental_health_live.csv'")
