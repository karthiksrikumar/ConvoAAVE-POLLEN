import os
import praw

# Configuration
REDDIT_CLIENT_ID = "YOUR_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDDIT_USER_AGENT = "iLeaving_Anonomoys"
SUBREDDITS = ["BlackPeopleTwitter", "BlackCulture"]
POST_LIMIT = 500
COMMENT_LIMIT = 500
OUTPUT_DIR = "data/raw/conversational/"
OUTPUT_FILE = "reddit_aave.txt"

def scrape_reddit(client_id: str, client_secret: str, user_agent: str,
                  subreddits: list, post_limit: int, comment_limit: int,
                  output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    collected = []
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        # Posts
        for submission in subreddit.hot(limit=post_limit):
            text = f"{submission.title} {submission.selftext or ''}".strip().replace("\n", " ")
            collected.append(text)
        # Comments
        for comment in subreddit.comments(limit=comment_limit):
            collected.append(comment.body.replace("\n", " "))
    with open(output_path, "w", encoding="utf-8") as f:
        for line in collected:
            f.write(line + "\n")
    print(f"[Reddit] Saved {len(collected)} lines to {output_path}")

if __name__ == "__main__":
    out_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    scrape_reddit(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT,
                  SUBREDDITS, POST_LIMIT, COMMENT_LIMIT, out_path)
