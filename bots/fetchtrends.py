import logging
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def fetch_trends(api, place, count):
    logger.info(f"Fetching trends for place: {place}")
    trends_result = api.trends_place(place)
    data = trends_result[0]
    # grab the trends
    trends = data['trends']
    # grab the name from each trend
    names = [trend['name'] for trend in trends]
    trends_with_count = names[:count]
    trends_obj = ' '.join(trends_with_count)
    return trends_obj


def main():
    api = create_api()
    count = 5
    place = 23424863
    top_trends = fetch_trends(api, place, count)
    logger.info(f"Top trends: {top_trends}")


if __name__ == "__main__":
    main()
