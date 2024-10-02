import black
from flask import request
from markupy import html2markupy

from .flask import MarkupyFlask
from .views.components.code import CodeComponent
from .views.components.error import ErrorComponent
from .views.pages.home import HomePage

app = MarkupyFlask(__name__)


@app.route("/")
def home():
    return HomePage()


@app.route("/convert", methods=["POST"])
def convert():
    html_str = request.form["html"]
    format_output = bool(request.form.get("format"))
    use_selector = bool(request.form.get("selector"))
    use_import_tag = not bool(request.form.get("import"))
    try:
        markupy_str = html2markupy(
            html_str, use_selector=use_selector, use_import_tag=use_import_tag
        )
    except Exception as e:
        return ErrorComponent(str(e))
    else:
        if format_output:
            try:
                markupy_str = black.format_str(markupy_str, mode=black.Mode())
            except black.parsing.InvalidInput:
                pass

    return CodeComponent(code=markupy_str)
