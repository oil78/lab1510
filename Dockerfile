FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Use shell form so $PORT is evaluated correctly at runtime
CMD gunicorn --bind 0.0.0.0:${PORT} app:app
