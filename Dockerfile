FROM python:3.12-slim

# Avoid bytecode + ensure stdout/err is unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Workdir
WORKDIR /app

# Install runtime deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY src/ ./src/
RUN chmod +x /src/main.py

# Default entrypoint (args come after image name)
ENTRYPOINT ["python", "/src/main.py"]
