FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
COPY src .

RUN uv sync --frozen --no-dev
ENV PATH=/app/.venv/bin:$PATH

CMD ["uv", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "html2markupy:app"]