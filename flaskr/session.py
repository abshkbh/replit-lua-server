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

    def serialize_lua_result(self, lua_output) -> dict:
        """Serializes a Lua result passed as |lua_output| into a dictionary."""

        print(f'Type of {lua_output} is {type(lua_output)}')

        if lua_output is None:
            return {}

        # Bool check has to come before int check as "bool" also matches with isInstance of int.
        if isinstance(lua_output, bool):
            return {'ValueType': 'Boolean', 'Value': str(lua_output)}

        if isinstance(lua_output, int):
            return {'ValueType': 'Number', 'Value': lua_output}

        if isinstance(lua_output, str):
            return {'ValueType': 'String', 'Value': lua_output}

        raise ValueError(f"Can't serialize Lua output: {lua_output}")

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
