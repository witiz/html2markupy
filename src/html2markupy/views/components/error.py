from typing import override

from markupy import Node, View
from markupy.tag import Span


class ErrorComponent(View):
    def __init__(self, message: str) -> None:
        self.message = message

    @override
    def render(self) -> Node:
        return Span(style="color:red")[self.message]
