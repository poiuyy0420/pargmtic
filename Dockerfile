FROM python:3.9.0

WORKDIR /home/

RUN echo "testing1234"

RUN git clone https://github.com/poiuyy0420/pargmtic.git

WORKDIR /home/pargmtic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pargmtic.settings.deploy && python manage.py migrate --settings=pargmtic.settings.deploy && gunicorn pargmtic.wsgi --env DJANGO_SETTINGS_MODULE=pargmtic.settings.deploy --bind 0.0.0.0:8000"]
