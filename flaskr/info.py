from flask import Blueprint, jsonify

bp = Blueprint('info', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def root():
    """Returns a sanity check about the server running."""
    return jsonify({'output': 'Welcome to LUA evaluation server'})


@bp.route('/create_session', methods=['POST'])
def add():
    """Runs ls and returns the result"""
    return jsonify({'output': 'dummy_file.txt'})
