```dockerfile
# Use official Python runtime as base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p data/processed data/raw models logs

# Expose port for FastAPI application
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Alternative Dockerfile with development support:

```dockerfile
# Multi-stage build for production
FROM python:3.12-slim as production

# Set environment variables for production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p data/processed data/raw models logs

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run as non-root user for security
RUN useradd --create-home --shell /bin/bash app
USER app

# Production command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

# Development stage
FROM production as development

# Switch back to root to install dev dependencies
USER root

# Install development dependencies
RUN pip install --no-cache-dir pytest black flake8 mypy

# Create volume for development
VOLUME ["/app"]

# Development command with auto-reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

## Docker Compose file (docker-compose.yml) for reference:

```yaml
version: '3.8'

services:
  student-predictor:
    build:
      context: .
      target: production  # or 'development' for dev
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
      - PYTHONUNBUFFERED=1
    volumes:
      - ./data:/app/data
      - ./models:/app/models
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Optional: Add Redis for caching
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    restart: unless-stopped

  # Optional: Add PostgreSQL for data storage
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: student_db
      POSTGRES_USER: student_user
      POSTGRES_PASSWORD: student_pass
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  postgres_data:
```

## .dockerignore file (recommended):

```dockerignore
# Git
.git
.gitignore

# Python
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env
venv
.venv
pip-log.txt
pip-delete-this-directory.txt

# IDE
.vscode
.idea
*.swp
*.swo

# Testing
.coverage
.pytest_cache
htmlcov/

# Documentation
docs/_build

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Data (optional - exclude if you want to include sample data)
data/raw/
data/processed/

# Models (optional - exclude if you want to include pre-trained models)
models/
```

## Build and run commands:

```bash
# Build the Docker image
docker build -t student-performance-predictor .

# Run the container
docker run -d -p 8000:8000 --name student-predictor student-performance-predictor

# Run with volume mounts for data persistence
docker run -d -p 8000:8000 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/models:/app/models \
  --name student-predictor student-performance-predictor

# Run with environment variables
docker run -d -p 8000:8000 \
  -e ENVIRONMENT=production \
  -e MODEL_PATH=/app/models/best_model.pkl \
  --name student-predictor student-performance-predictor

# View logs
docker logs -f student-predictor

# Stop container
docker stop student-predictor

# Remove container
docker rm student-predictor
```

The Dockerfile includes:
- Multi-stage build for production and development
- Security best practices (non-root user, health checks)
- Efficient layer caching
- Proper environment configuration
- Health checks for container orchestration
- Support for both development and production environments