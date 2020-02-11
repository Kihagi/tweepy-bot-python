import logging
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def tweet(api, text):
    api.update_status(text)


def main():
    api = create_api()
    tweet_text = "This is a test tweet by Tweepy"
    logger.info(f"About to tweet: {tweet_text}")
    tweet(api, tweet_text)


if __name__ == "__main__":
    main()
