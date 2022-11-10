FROM python:3.9

WORKDIR /ire_site
COPY ./ire_site/requirements.txt /ire_site/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
COPY ./ire_site /ire_site

EXPOSE 8000
CMD ["python3", "manage.py", "runserver"]