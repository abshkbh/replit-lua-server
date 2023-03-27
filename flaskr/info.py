from flask import Blueprint, jsonify
from flaskr import global_state

bp = Blueprint('info', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def root():
    """Returns a sanity check about the server running."""
    return jsonify({'output': 'Welcome to LUA evaluation server'})


@bp.route('/create_session', methods=['POST'])
def add():
    """Creates a new session."""

    session_id = global_state.SERVER_STATE.create_session()
    return jsonify({'id': session_id})
