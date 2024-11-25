FROM python:3.12-slim as base

WORKDIR /app

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


COPY pyproject.toml poetry.lock ./


RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY ./src ./src
COPY ./main.py ./

EXPOSE 8080

CMD ["poetry", "run", "python", "main.py"]
