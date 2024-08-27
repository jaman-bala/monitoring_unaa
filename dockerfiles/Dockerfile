# Use the official Python base image
FROM python:3.9-alpine3.12

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    cargo  # Install Rust and Cargo for compiling Rust extensions

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
