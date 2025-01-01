# Base Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY dashboard.py /app/
COPY requirements.txt /app/

# Install build-essential tools and dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    libssl-dev \
    && apt-get clean

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Run the Flask application
CMD ["python", "dashboard.py"]
