FROM python:3.8.5-alpine

WORKDIR /usr/src/showsite

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN \
 apk add --no-cache python3 postgresql-libs linux-headers && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .
CMD sh -c ''exec psql -h "db" -p "5432" -U postgres''