FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /project

COPY . /project

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv sync

ARG INPUT_FILE
ARG OUTPUT_FILE

ENTRYPOINT sh -c 'uv run run.py predict --input-file "$INPUT_FILE" --output-file "$OUTPUT_FILE"'
