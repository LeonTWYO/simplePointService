# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r app/requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 8080

# # Define the command to run your application
# CMD ["python", "app.py"]
