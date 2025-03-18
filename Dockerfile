# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code into the container
COPY . .

# Run tests by default (adjust command as needed)
# CMD ["python", "-m", "unittest", "discover"]
CMD ["python", "test_runner.py"]
