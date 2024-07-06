# Use the official Python image from the Docker Hub with Python 3.10
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


