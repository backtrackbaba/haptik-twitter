from flask import render_template
from flask_login import login_required, current_user

from src.dashboard import bp
from src.dashboard.forms import CreateTweetForm
from src.tweet.service import TweetService
from src.user.service import UserService


@bp.route('/')
@login_required
def feed():
    """
    This is the main feed page similar to Twitter's Home page
    """
    user_service = UserService()
    tweet_form = CreateTweetForm()
    user = user_service.get_user_from_id(current_user.id)
    tweets = user.followed_posts().all()
    ids = []
    for tweet in tweets:
        ids.append(tweet.user_id)
    ids_mapping = user_service.get_users_from_ids(ids)
    return render_template('pages/dashboard/index.html', tweet_form=tweet_form, tweets=tweets, user=user,
                           ids_mapping=ids_mapping)


@bp.route('/profile')
@login_required
def profile():
    """
    Profile page of the logged_in user
    """
    tweet_service = TweetService()
    tweets = tweet_service.get_tweets_by_user_id(current_user.id)
    return render_template('pages/dashboard/profile.html', tweets=tweets, user=current_user)


@bp.route('/users')
@login_required
def users():
    """
    Listing of all users with a link to their profile
    """
    user_service = UserService()
    users = user_service.get_all_users()
    return render_template('pages/dashboard/users.html', users=users)


@bp.route('/users/<username>')
@login_required
def user_profile(username):
    """
    Profile page for all users
    """
    user_service = UserService()
    tweet_service = TweetService()
    user = user_service.get_user_from_username(username)
    tweets = tweet_service.get_tweets_by_user_id(user.id)
    return render_template('pages/dashboard/profile.html', tweets=tweets, user=user)
