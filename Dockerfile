FROM python:3.9-slim-buster

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD [ "gunicorn", "trash_map.wsgi:application", "--bind", "0.0.0.0:8000" ]