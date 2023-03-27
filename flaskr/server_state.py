from flaskr import session


class ServerState():
    """
    Maintains the state associated with a server and isn't persisted in memory.
    """

    def __init__(self):
        # The id to allocate to the next session.
        self.__next_session_id = 1

        # This will contain the mapping of a session id to |Session| object.
        self.__session_id_to_session = {}

    def get_and_increment_next_session_id(self):
        "Returns the next session id and increments it."

        result = self.__next_session_id
        self.__next_session_id += 1
        return result

    def get_session(self, session_id: int):
        "Returns the |Session| corresponding to a |session_id|."

        if session_id in self.__session_id_to_session:
            return self.__session_id_to_session[session_id]
        raise ValueError(f'Invalid session id:{session_id}')

    def create_new_session(self) -> int:
        "Creates a new session and returns its allocated id"

        new_session_id = self.get_and_increment_next_session_id()
        self.__session_id_to_session[new_session_id] = session.Session()
        return new_session_id
