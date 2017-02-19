FROM python:3.6.0
MAINTAINER Benoit Brayer <https://github.com/M0dM>

WORKDIR /usr/share/django/
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "/usr/share/django/manage.py", "runserver", "8000"]
