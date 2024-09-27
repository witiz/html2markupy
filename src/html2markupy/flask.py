from flask import Flask, Response

from markupy import View


class MarkupyFlask(Flask):
    # Here we override make_response to be able to return View instances
    # from our routes directly without having to cast them to str()
    def make_response(self, rv):
        if isinstance(rv, View):
            return Response(rv.render())
        return super().make_response(rv)
