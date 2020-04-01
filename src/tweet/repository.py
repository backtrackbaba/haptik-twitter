from typing import List

from sqlalchemy import desc

from src.models.tweet import Tweet


class TweetRepository:

    def get_tweets_by_user_id(self, id) -> List:
        return Tweet.query.filter(Tweet.user_id == id).order_by(desc(Tweet.created_at)).all()
