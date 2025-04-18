FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /project

COPY . /project

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv sync

ENTRYPOINT ["uv", "run", "python", "run.py"]
