FROM python:3.9-alpine3.12
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek

RUN apk add --no-cache \
    build-base \
    postgresql-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    imagemagick-dev \
    zlib-dev \
    file \
    make \
    python3-dev \
    && rm -rf /var/cache/apk/*

# Добавляем инструменты для компиляции Rust
RUN apk add --no-cache rust cargo

RUN pip install --upgrade pip && pip install uvicorn

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "./dockerfiles/docker-entrypoint.sh"]
