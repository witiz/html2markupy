from flask import Flask
from markupy import Component


class MarkupyFlask(Flask):
    # Here we override make_response to be able to return Component instances
    # from our routes directly without having to cast them to str()
    def make_response(self, rv):
        if isinstance(rv, Component):
            return super().make_response(str(rv))
        return super().make_response(rv)
