FROM python:3.9-slim-buster

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD [ "python3", "./picasso_test_project/manage.py", "runserver", "0.0.0.0:8000" ]