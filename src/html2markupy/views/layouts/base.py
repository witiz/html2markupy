from flask import url_for
from markupsafe import Markup
from markupy import Component, Node
from markupy import __version__ as markupy_version
from markupy.tag import (
    H1,
    A,
    Body,
    Footer,
    Head,
    Header,
    Hgroup,
    Html,
    Li,
    Link,
    Main,
    Meta,
    Nav,
    P,
    Script,
    Small,
    Title,
    Ul,
)


class BaseLayout(Component):
    def render(self) -> Node:
        return Html[
            Head[
                Meta(charset="utf8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1"),
                Title["html2markupy | Convert HTML to markupy"],
                Link(
                    rel="stylesheet",
                    href=url_for(
                        "static",
                        filename="vendor/prismjs-1.29.0/prism.css",
                    ),
                ),
                Link(
                    rel="stylesheet",
                    href=url_for("static", filename="vendor/pico-2.0.6.css"),
                ),
                Link(
                    rel="stylesheet",
                    href=url_for("static", filename="css/main.css"),
                ),
                Script(src=url_for("static", filename="vendor/htmx-2.0.2.js")),
                Script(
                    src=url_for(
                        "static",
                        filename="vendor/prismjs-1.29.0/prism.js",
                    )
                ),
                Script(
                    async_=True,
                    src="https://www.googletagmanager.com/gtag/js?id=G-VP8ZZRV4WR",
                ),
                Script[
                    Markup("""
                    window.dataLayer = window.dataLayer || [];
                    function gtag(){dataLayer.push(arguments);}
                    gtag('js', new Date());
                    gtag('config', 'G-VP8ZZRV4WR');
                    """)
                ],
            ],
            Body[
                Header(".container")[self.header()],
                Main(".container")[self.main()],
                Footer(".container", style="text-align:center")[self.footer()],
            ],
        ]

    def header(self) -> Node:
        return Nav[
            Hgroup[
                H1["html2markupy"],
                P["Convert HTML to markupy"],
            ],
            Ul[
                Li[
                    A(href="https://github.com/witiz/markupy", target="_blank")[
                        "markupy on Github"
                    ]
                ],
                Li[
                    A(href="https://github.com/witiz/html2markupy", target="_blank")[
                        "view source"
                    ]
                ],
            ],
        ]

    def main(self) -> Node:
        return None

    def footer(self) -> Node:
        return Small[
            "Powered by ",
            A(href="https://github.com/witiz/markupy", target="_blank")[
                f"markupy v{markupy_version}"
            ],
        ]
