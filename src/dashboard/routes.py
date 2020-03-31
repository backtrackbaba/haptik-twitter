from typing import List

from flask import render_template
from flask_login import login_required, current_user

from src.dashboard import bp
from src.dashboard.forms import CreateTweetForm
from src.models.tweet import Tweet
from src.models.user import User


@bp.route('/')
@login_required
def feed():
    tweet_form = CreateTweetForm()
    user = User.query.filter_by(id=current_user.id).first_or_404()
    tweets = user.followed_posts().all()
    ids = []
    for tweet in tweets:
        ids.append(tweet.user_id)
    ids_mapping = get_ids_mapping(ids)
    return render_template('pages/dashboard/index.html', tweet_form=tweet_form, tweets=tweets, user=user,
                           ids_mapping=ids_mapping)


@bp.route('/profile')
@login_required
def profile():
    tweets = Tweet.query.filter(Tweet.user_id == current_user.id).all()
    print('tweets', tweets)
    return render_template('pages/dashboard/profile.html', tweets=tweets, user=current_user)


@bp.route('/users')
@login_required
def users():
    """
    Listing of all users with a link to their profile
    """
    users = User.query.all()
    return render_template('pages/dashboard/users.html', users=users)


@bp.route('/users/<username>')
@login_required
def user_profile(username):
    """
    Profile page of all users
    """
    user = User.query.filter_by(username=username).first()
    tweets = Tweet.query.filter(Tweet.user_id == user.id).all()
    return render_template('pages/dashboard/profile.html', tweets=tweets, user=user)


def get_ids_mapping(ids: List):
    ids_mapping = {}
    for id in ids:
        user = User.query.filter_by(id=id).first()
        ids_mapping[id] = user
    return ids_mapping
