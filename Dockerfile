# Use official Python base image
FROM python:3.13-alpine

# Set environment vars
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1 
# Allows you to see logs in real-time when running the container
ENV PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose port
EXPOSE 8000

# Start FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]