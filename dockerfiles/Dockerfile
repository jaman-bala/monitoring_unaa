FROM python:3.9-alpine3.12
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek

RUN apk add --no-cache build-base \
    gcc postgresql-dev \
    linux-headers musl-dev libffi-dev \
    libxml2-dev libxslt-dev imagemagick-dev \
    zlib-dev py3-magic make \
    && rm -rf /var/apt/list/*

# Установка Gunicorn
RUN pip install --upgrade pip && pip install gunicorn

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "./dockerfiles/docker-entrypoint.sh"]
