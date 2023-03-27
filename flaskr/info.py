from flask import Blueprint, jsonify, request, abort
from flaskr import server_state

# TODO: Move global object initialization in init to be used by other endpoint collections as well.
SERVER_STATE = server_state.ServerState()
bp = Blueprint('info', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def root():
    """Returns a sanity check about the server running."""
    return jsonify({'output': 'Welcome to LUA evaluation server'})


@bp.route('/create_session', methods=['POST'])
def create_session():
    """Creates a new session."""

    session_id = SERVER_STATE.create_new_session()
    return jsonify({'id': session_id})


@bp.route('/evaluate/<int:session_id>', methods=['POST'])
def evaluate(session_id):
    """Evaluates an expression at the server with id=|id|."""
    request_json = request.get_json()
    if not request_json:
        abort(400, {'error': 'no JSON data in the request'})

    expression = request_json.get('expression')
    if not expression:
        abort(400, {'error': 'no expression provided to evaluate'})

    try:
        session = SERVER_STATE.get_session(session_id)
    except ValueError as _:
        abort(400, {'error': f'invalid session id={id}'})

    print(f'Going to evaluate expression={expression} on session id={id}')
    return jsonify()
