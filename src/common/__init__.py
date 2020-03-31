from flask import Blueprint

bp = Blueprint('common', __name__)

from src.common import routes
