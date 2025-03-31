from flask import Flask
from flask.typing import ResponseReturnValue
from markupy import View


class MarkupyFlask(Flask):
    # Here we override make_response to be able to return Component instances
    # from our routes directly without having to cast them to str()
    def make_response(self, rv: ResponseReturnValue):
        if isinstance(rv, View):
            rv = str(rv)
        return super().make_response(rv)
