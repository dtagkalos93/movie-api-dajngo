FROM python:3.10.4-slim-buster

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y libpq-dev
RUN apt-get install -y sqlite3
RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app

COPY ./poetry.lock ${WORKDIR}/poetry.lock
COPY ./pyproject.toml ${WORKDIR}/pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . .

ENTRYPOINT ["/app/compose/django_start"]
