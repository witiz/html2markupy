from typing import override

from flask import url_for

from markupy import Node
from markupy.tag import (
    Button,
    Div,
    Fieldset,
    Form,
    Input,
    Label,
    P,
    Pre,
    Section,
    Textarea,
)

from ..layouts.base import BaseLayout


class HomePage(BaseLayout):
    @override
    def main(self) -> Node:
        return [
            Section[
                P[
                    "html2markupy allows you to experiment with the markupy syntax, and will help you translate existing HTML snippets if you decide to migrate."
                ],
                P[
                    "The conversion is actually performed by the markupy library itself which provides a html2markupy command line tool that you can run in a terminal."
                ],
            ],
            Form(
                "#form",
                hxPost=url_for("convert"),
                hxTarget="#markupy",
                hxSwap="innerHTML",
                hxTrigger="submit, change from:input",
            )[
                Div(".grid")[
                    Textarea(
                        "#html",
                        name="html",
                        placeholder="Type or copy/paste HTML code here...",
                        spellcheck="false",
                        rows=20,
                    ),
                    Pre(
                        "#markupy",
                        hxOn__htmx__afterSettle="Prism.highlightAll();",
                    )["...and the markupy equivalent will appear here."],
                ],
                Div(".grid")[
                    Fieldset[
                        Label[
                            Input(type="checkbox", name="format", checked=True),
                            "Format output",
                        ],
                        Label[
                            Input(type="checkbox", name="selector", checked=True),
                            "Use selector syntax for id/class attributes",
                        ],
                        Label[
                            Input(type="checkbox", name="import", checked=True),
                            "Use individual tag imports",
                        ],
                    ],
                    Button(type="submit")["Convert to markupy"],
                ],
            ],
        ]
