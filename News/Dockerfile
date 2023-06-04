FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/dm_rest
RUN pip install psycopg2
RUN pip install django-debug-toolbar
RUN pip install pillow
RUN pip install django
COPY . /usr/src/dm_rest
#EXPOSE 8000
#CMD ["python","manage.py", "runserver", "127.0.0.1:8000"]