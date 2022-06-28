FROM python:3.10.5-slim-buster AS poetry
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock .
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.10.5-slim-buster
WORKDIR /app
RUN apt-get update
RUN apt-get install git gcc python3-dev libpq-dev -y
RUN apt-get clean -y
COPY --from=poetry /app/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]