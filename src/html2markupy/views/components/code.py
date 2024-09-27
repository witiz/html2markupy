from typing import override

from markupy import Node, View
from markupy.tag import Code


class CodeComponent(View):
    def __init__(self, code: str) -> None:
        self.code = code

    @override
    def render(self) -> Node:
        return Code(".language-python")[self.code]
