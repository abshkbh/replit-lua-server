import lupa
from lupa import LuaRuntime, LuaSyntaxError


class Session():
    """
    Maintains the state associated with a server and isn't persisted in memory. Currently, is only used to evaluate Lua expressions.
    """

    def __init__(self, session_id):
        # ID of this session.
        self.__session_id = session_id

        # The object to evaluate the expression.
        self.__lua_runtime = LuaRuntime()

    def serialize_lua_result(self, result) -> dict:
        """Serializes a Lua result into a dictionary."""
        return {}

    def evaluate(self, expression: str) -> dict:
        """
        Evaluates the given expression. Throws a ValueError if there was an error while
        executing.
        """

        try:
            result = self.__lua_runtime.execute(expression)
        except LuaSyntaxError as exception:
            raise ValueError(f'Syntax error:{exception}') from exception
        print(f'{expression} = {result}')
        return self.serialize_lua_result(result)
