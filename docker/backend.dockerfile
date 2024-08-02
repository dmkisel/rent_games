FROM ubuntu:latest

COPY ../poetry.lock /app
COPY ../pyproject.toml /app
COPY ../backend/ /app

WORKDIR app




CMD ["streamlit", "run", "app.py"]