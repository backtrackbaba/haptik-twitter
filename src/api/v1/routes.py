from flask import request
from flask_login import current_user, login_required

from src import db
from src.api.v1 import bp
from src.models.tweet import Tweet
from src.tweet.service import TweetService
from src.user.service import UserService


@bp.route('/tweet', methods=['POST'])
@login_required
def create_tweet():
    user_id = current_user.id
    tweet_text = request.form.get('body')
    if user_id:
        if len(tweet_text) <= 140:
            user_id = current_user.id

            tweet = Tweet()
            tweet.user_id = user_id
            tweet.body = tweet_text

            db.session.add(tweet)
            db.session.commit()

            response = {'status': 200, 'error_message': ""}
            return response, 200
        response = {'status': 400, 'error_message': "Form data invalid"}
        return response, 400
    response = {'status': 401, 'error_message': "Unauthorized User"}
    return response, 401


@bp.route('/<username>/follow', methods=['POST'])
@login_required
def follow_user(username):
    user_service = UserService()
    user = user_service.get_user_from_username(username)
    if user is None:
        response = {'status': 404, 'error_message': "User not found"}
        return response, 404
    if user == current_user:
        response = {'status': 400, 'error_message': "You can't follow yourself!"}
        return response, 400
    current_user.follow(user)
    db.session.commit()
    response = {'status': 200, 'error_message': "User followed!"}
    return response, 200


@bp.route('/<username>/unfollow', methods=['POST'])
@login_required
def unfollow_user(username):
    user_service = UserService()
    user = user_service.get_user_from_username(username)
    if user is None:
        response = {'status': 404, 'error_message': "User not found"}
        return response, 404
    if user == current_user:
        response = {'status': 400, 'error_message': "You can't follow yourself!"}
        return response, 400
    current_user.unfollow(user)
    db.session.commit()
    response = {'status': 200, 'error_message': "User successfully unfollowed!"}
    return response, 200


@bp.route('/feed', methods=['GET'])
@login_required
def get_tweet_feed():
    tweet_service = TweetService()
    tweets = tweet_service.get_tweets_by_user_id(current_user.id)
    tweets_list = []
    for tweet in tweets:
        tweets_list.append(_tweet_to_json(tweet))
    print(tweets)

    data = {
        'user_id': current_user.id,
        'tweets': tweets_list
    }
    return data


def _tweet_to_json(tweet):
    data = {
        'tweet_id': tweet.id,
        'tweet_body': tweet.body,
        'tweet_created_at': str(tweet.created_at),
        'tweet.user_id': tweet.user_id,
    }
    return data
