from markupy import Component, View
from markupy.elements import Span


class ErrorComponent(Component):
    def __init__(self, *, message: str) -> None:
        super().__init__()
        self.message = message

    def render(self) -> View:
        return Span(style="color:red")[self.message]
