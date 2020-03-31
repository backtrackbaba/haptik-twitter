from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api/v1')

from src.api.v1 import routes
