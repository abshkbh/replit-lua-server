class Session():
    """
    Maintains the state associated with a server and isn't persisted in memory.
    """

    def __init__(self, session_id):
        # ID of this session.
        self.__session_id = session_id

        # The object to evaluate the expression.
        self.__eval_object = None
