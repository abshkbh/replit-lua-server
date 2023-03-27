from flask import Blueprint, jsonify
from flaskr import server_state

# TODO: Move global object initialization in init to be used by other endpoint collections as well.
SERVER_STATE = server_state.ServerState()
bp = Blueprint('info', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def root():
    """Returns a sanity check about the server running."""
    return jsonify({'output': 'Welcome to LUA evaluation server'})


@bp.route('/create_session', methods=['POST'])
def add():
    """Creates a new session."""

    session_id = SERVER_STATE.create_new_session()
    return jsonify({'id': session_id})
