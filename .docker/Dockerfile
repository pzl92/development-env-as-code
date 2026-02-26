FROM python:3.14-slim AS base

ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG WORKDIR=/app

WORKDIR $WORKDIR

RUN apt-get update && apt-get install -y --no-install-recommends \
  git curl build-essential \
  && rm -rf /var/lib/apt/lists/*

RUN adduser -u $USER_UID --disabled-password --gecos "" $USERNAME && chown -R $USERNAME $WORKDIR

USER $USERNAME

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \ 
  POETRY_NO_INTERACTION=1 \
  POETRY_VERSION=2.3.2

RUN python -m venv $WORKDIR/.venv
RUN chown -R $USER_UID:$USER_GID $WORKDIR/.venv
RUN . $WORKDIR/.venv/bin/activate && pip install "poetry==$POETRY_VERSION"

ENV PATH="$WORKDIR/.venv/bin:$PATH"

COPY pyproject.toml poetry.lock /app/
COPY sample_app /app/sample_app

RUN poetry install
