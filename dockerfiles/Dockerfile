FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek
# Install system dependencies
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    && rm -rf /var/cache/apk/*

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy rest of the application code
COPY . .

# Expose port
EXPOSE 8000

# Run command
ENTRYPOINT ["sh", "./dockerfiles/docker-entrypoint.sh"]
