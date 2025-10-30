# Start with a small, stable Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port where the Flask application runs
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"]