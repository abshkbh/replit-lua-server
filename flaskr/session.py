import lupa
from lupa import LuaRuntime, LuaSyntaxError


class Session():
    """
    Maintains the state associated with a server and isn't persisted in memory. Currently, is only used to evaluate Lua expressions.
    """

    def __init__(self):
        # The object to evaluate the expression.
        self.__lua_runtime = LuaRuntime()

    # TODO: Move this to a helper class.
    def serialize_lua_table(self, lua_output, parent_table_ids) -> dict:
        """Serializes a Lua table and returns a dictionary."""
        print(f'Table items are {list(lua_output.items())}')

        # Values would be a list of dicts [{}, {}]. Go over each key value pair and get a dictionary
        # consiting of the key, value and their representation as one dictionary. Add this
        # dictionary to |table_values|, this would be the value of a table.
        table_values = []
        table_id = str(lua_output)
        parent_table_ids.add(table_id)
        for key, value in list(lua_output.items()):
            print(f'Key={key} Value={value}')
            # Since these are key, value pairs for a table they need different identifiers in their
            # dictionary representation to delinate which is the Key and which is the value.
            key_dict = self.serialize_lua_result(
                key, parent_table_ids, "KeyType", "KeyValue")
            value_dict = self.serialize_lua_result(
                value, parent_table_ids, "ValueType", "ValueValue")
            key_dict.update(value_dict)
            table_values.append(key_dict)
        print(f'Table Values  = {table_values}')
        return {'Type': 'Table', 'Id': str(lua_output), 'Value': table_values}

    # TODO: Move this to a helper class.
    def serialize_lua_result(self, lua_output, parent_table_ids, type_key=None, value_key=None) -> dict:
        """
        Serializes a Lua result passed as |lua_output| into a dictionary. lua_output: Result of a
        Lua evaluation.

        type_key: An optional string to be used in the final dict for the Lua type.

        value_key: An optional string to be used in the final dict for the Lua types value.

        parent_table_ids: A set of table ids seen before this.
        """

        print(f'Type of {lua_output} is {type(lua_output)}')

        if lua_output is None:
            return {}

        if not type_key:
            type_key = "Type"

        if not value_key:
            value_key = "Value"

        # Bool check has to come before int check as "bool" also matches with isInstance of int.
        if isinstance(lua_output, bool):
            return {type_key: 'Boolean', value_key: str(lua_output)}

        if isinstance(lua_output, int):
            return {type_key: 'Number', value_key: lua_output}

        if isinstance(lua_output, str):
            return {type_key: 'String', value_key: lua_output}

        # If we're called recursively from |serialize_lua_table| we may refer to ourselves, in this
        # case we need a check to stop recursing infinitely. This clauses just puts a reference to
        # the parent instead of going in an endless loop.
        table_id = str(lua_output)
        if table_id in parent_table_ids:
            print(f'Table id={table_id} is present in set')
            return {type_key: 'TableRef', value_key: table_id}

        return self.serialize_lua_table(lua_output, parent_table_ids)

        # TODO: Add concerete check for 'table' type and re-add this.
        # raise ValueError(f"Can't serialize Lua output: {lua_output}")

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
        return self.serialize_lua_result(result, set())
