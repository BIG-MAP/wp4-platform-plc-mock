FROM python:3.11.3-slim

ADD . /app

WORKDIR /app
RUN pip install poetry
RUN poetry install

ENV PYTHONUNBUFFERED=1
ENV PORT=4840

EXPOSE $PORT

CMD ["poetry", "run", "python", "main.py"]