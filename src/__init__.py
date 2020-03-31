import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from walrus import Database

from src.config import Config

db = SQLAlchemy()
migrate = Migrate()
redis_db = Database(host=os.environ.get('CACHE_REDIS_HOST'), port=os.environ.get('CACHE_REDIS_PORT'),
                    db=os.environ.get('CACHE_REDIS_DB'), password=os.environ.get('CACHE_REDIS_PASSWORD'))
cache = redis_db.cache(default_timeout=int(os.environ.get('CACHE_REDIS_TIMEOUT')))

login = LoginManager()
login.login_view = 'auth.login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from src.common import bp as common_bp
    app.register_blueprint(common_bp)

    from src.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from src.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp)

    from src.api.v1 import bp as api_bp
    app.register_blueprint(api_bp)

    from src.utils.template_filters import get_relative_time
    app.jinja_env.filters['get_relative_time'] = get_relative_time

    return app


from src.models import user, tweet

print(user, tweet)
