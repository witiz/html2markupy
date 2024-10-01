from markupy import Component, Node
from markupy.tag import Code


class CodeComponent(Component):
    def __init__(self, code: str) -> None:
        self.code = code

    def render(self) -> Node:
        return Code(".language-python")[self.code]
