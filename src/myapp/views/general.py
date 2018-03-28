from flask import Blueprint, render_template, jsonify
from datetime import datetime


mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    return render_template('general/index.html')


@mod.route('/data')
def get_data():
    data = [
        {'#': 1, 'First': 'Mark', 'Last': 'Otto'},
        {'#': 2, 'First': 'Jacob', 'Last': 'Thornton'},
        {'#': 3, 'First': 'Larry', 'Last': 'Bird'}
    ]
    return jsonify(data)


@mod.errorhandler(404)
def not_found():
    return render_template('404.html'), 404


@mod.context_processor
def current_year():
    return {'current_year': datetime.utcnow().year}
