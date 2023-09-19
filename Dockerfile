# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in docker
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade -r requirements.txt

# Define environment variable
ENV NAME World

# Run your script when the container launches
CMD ["python3", "main2.py"]
