FROM python:3.9.0

WORKDIR /home/

RUN echo "qwerasgsfhsdfh"

RUN git clone https://github.com/taroun/new_1ban.git

WORKDIR /home/new_1ban/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=new_1ban.settings.deploy && python manage.py migrate --settings=new_1ban.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=new_1ban.settings.deploy new_1ban.wsgi --bind 0.0.0.0:8000"]