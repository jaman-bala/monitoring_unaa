# Устанавливаем базовую образу Alpine Linux
FROM python:3.10-slim-buster AS builder

# Устанавливаем зависимости для сборки
RUN apk add --no-cache \
        build-base \
        gcc \
        g++ \
        git \
        python3-dev \
        libffi-dev \
        openssl-dev \
        postgresql-dev \
        jpeg-turbo-dev \
        zlib-dev \
        libxml2-dev \
        libxslt-dev \
        libpqxx-dev \
        musl-dev \
        libc-dev \
        linux-headers \
        curl \
        wget \
        bash \
        openssh-client \
        sudo \
        ca-certificates \
        && rm -rf /var/cache/apk/*

# Устанавливаем зависимости из requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Создаем рабочую директорию и копируем исходный код
WORKDIR /app
COPY . .

# Компиляция и установка Python пакетов
RUN pip install --no-cache-dir -r requirements.txt


# Добавляем переменные окружения
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Устанавливаем Gunicorn
RUN pip install gunicorn


EXPOSE 8000

ENTRYPOINT ["sh", "./dockerfiles/docker-entrypoint.sh"]
