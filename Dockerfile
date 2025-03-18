# Use Alpine Linux as the base image
FROM python:3.12-alpine

# Set working directory
WORKDIR /app

# Install dependencies
RUN apk add --no-cache build-base

# Copy script and requirements
COPY starship_scanner.py requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define entrypoint
ENTRYPOINT ["python3", "starship_scanner.py"]
