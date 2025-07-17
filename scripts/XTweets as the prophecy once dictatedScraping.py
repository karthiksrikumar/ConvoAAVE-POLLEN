```python
#!/usr/bin/env python3
"""
Scrape AAVE Tweets using snscrape.
Save as: data/raw/conversational/tweets_aave.txt
"""

import os
import snscrape.modules.twitter as sntwitter

# Configuration
TWITTER_QUERY = "(finna OR ion OR tryna OR 'he be' OR 'she be' OR 'ain’t never') lang:en"
TWITTER_MAX_TWEETS = 250
OUTPUT_DIR = "data/raw/conversational/"
OUTPUT_FILE = "tweets_aave.txt"

def scrape_tweets(query: str, max_tweets: int, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets.append(tweet.content.replace("\n", " "))
    with open(output_path, "w", encoding="utf-8") as f:
        for line in tweets:
            f.write(line + "\n")
    print("[Tweets] Saved {len(tweets)} tweets to {output_path}")

if __name__ == "__main__":
    out_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    scrape_tweets(TWITTER_QUERY, TWITTER_MAX_TWEETS, out_path)
