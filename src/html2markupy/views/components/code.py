from markupy import Component, View
from markupy.tag import Code


class CodeComponent(Component):
    def __init__(self, code: str) -> None:
        super().__init__()
        self.code = code

    def render(self) -> View:
        return Code(".language-python")[self.code]
