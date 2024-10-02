from typing import override

from flask import url_for
from markupy import Node
from markupy.tag import (
    A,
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

default_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>html2markupy</title>
</head>
<body>
    <header>
        <h1 class="heading">Welcome to html2markupy!</h1>
    </header>
    <main id="container">
        Discover a powerful way to build your HTML pages and components in Python!
    </main>
    <footer>
        Powered by <a href="https://markupy.witiz.com">markupy</a>
    </footer>
</body>
</html>
"""


class HomePage(BaseLayout):
    @override
    def main(self) -> Node:
        return [
            Section[
                P[
                    "html2markupy allows you to experiment with the markupy syntax, and will help you translate existing HTML snippets if you decide to migrate."
                ],
                P[
                    "The conversion is actually performed by the markupy library itself which also provides a ",
                    A(href="https://markupy.witiz.com/html2markupy", target="_blank")[
                        "html2markupy command line tool"
                    ],
                    " that you can run in a terminal.",
                ],
            ],
            Form(
                "#form",
                hxPost=url_for("convert"),
                hxTarget="#markupy",
                hxSwap="innerHTML",
                hxTrigger="load, submit, change from:input",
            )[
                Div(".grid")[
                    Textarea(
                        "#html",
                        name="html",
                        placeholder="Type or copy/paste HTML code here...",
                        spellcheck="false",
                        rows=20,
                        autofocus=True,
                    )[default_html],
                    Pre(
                        "#markupy",
                        hxOn__htmx__afterSettle="Prism.highlightAll();",
                    )["...and the markupy equivalent will appear here."],
                ],
                Div(".grid")[
                    Button(type="submit")["Convert to markupy"],
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
                ],
            ],
        ]
