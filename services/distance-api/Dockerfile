# Download base image python:3.9-slim
FROM python:3.9-slim

# Copy requirements file
COPY requirements.txt /app/requirements.txt

# Change workdir to /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Set Pythonpath
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Copy files to /app
COPY . /app

# Make entrypoint.sh script executable
RUN chmod +x /app/entrypoint.sh

# Set container to run as an executable
ENTRYPOINT ["/app/entrypoint.sh"]