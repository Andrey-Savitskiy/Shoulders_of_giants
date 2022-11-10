FROM python:3.9

WORKDIR /ire_site
COPY ./requirements.txt /ire_site/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
COPY ./ire_site /ire_site

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000