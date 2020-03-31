import click

from src.models.tweet import Tweet
from src.models.user import User


def register(app):
    @app.cli.group()
    def database():
        """Database related commands"""
        pass

    @database.command()
    @click.argument('clean')
    def clean(db):
        """Cleans the database and gets back to square one"""
        db.session.query(User).delete()
        db.session.query(Tweet).delete()
        db.session.commit()
