class ServerState():
    """
    Maintains the state associated with a server and isn't persisted in memory.
    """

    def __init__(self):
        # The id to allocate to the next session.
        self.__next_session_id = 1

        # This will contain the mapping of a session id to a stateful  object to evaluate the
        # expression sent by the client.
        self.__session_id_to_eval_object = {}

    def get_and_increment_next_session_id(self):
        "Returns the next session id and increments it."

        result = self.__next_session_id
        self.__next_session_id += 1
        return result

    def get_eval_obj(self, session_id: int):
        "Returns the evaluation object for a session."

        if session_id in self.__session_id_to_eval_object:
            return self.__session_id_to_eval_object[session_id]
        raise ValueError(f'Invalid session id:{session_id}')
