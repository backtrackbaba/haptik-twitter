from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators


class CreateTweetForm(FlaskForm):
    body = TextAreaField('Tweet', [validators.required(), validators.length(max=140)])
