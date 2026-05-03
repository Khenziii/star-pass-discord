FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main --no-root && \
    rm -rf /root/.cache/pypoetry

COPY . .

RUN poetry install --only-root

CMD ["poetry", "run", "star-pass-discord"]
