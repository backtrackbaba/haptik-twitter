from typing import List

from src.tweet.repository import TweetRepository


class TweetService:
    def __init__(self):
        self.tweet_repository = TweetRepository()

    def get_tweets_by_user_id(self, id) -> List:
        """
        Get tweets by user id. To be cached similar to User service and purging to be managed by save_tweet method
        """
        return self.tweet_repository.get_tweets_by_user_id(id)

    def save_tweet(self):
        """
        Save Tweet and purge tweets cache for that user. This will work as cache invalidator for the tweets service
        """
        raise NotImplementedError
