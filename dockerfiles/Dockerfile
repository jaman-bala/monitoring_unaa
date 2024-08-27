FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip
RUN pip cache purge

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-binary :all: cryptography
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "./dockerfiles/docker-entrypoint.sh"]
