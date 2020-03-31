from flask import render_template

from src.common import bp


@bp.route('/')
def home():
    return render_template('pages/common/index.html')
