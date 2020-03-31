from flask import request
from flask_login import current_user

from src import db
from src.api.v1 import bp
from src.models.tweet import Tweet
from src.models.user import User


@bp.route('/tweet', methods=['POST'])
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
def follow_user(username):
    user = User.query.filter_by(username=username).first()
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
def unfollow_user(username):
    user = User.query.filter_by(username=username).first()
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


@bp.route('/tweet', methods=['GET'])
def get_tweets():
    # TODO: Implement the same logic used to get tweeet in the template!
    pass
