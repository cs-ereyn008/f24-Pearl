FROM python:3.9-slim

WORKDIR /usr/src/app

COPY ./DjangoWork/requirements.txt .

RUN pip install -r requirements.txt

COPY ./DjangoWork .

EXPOSE 3000

CMD ["sh","-c", "python manage.py migrate && python manage.py runserver"]
