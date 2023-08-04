# Use an official Python runtime as a parent image
FROM python:3.9.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available outside this container
EXPOSE 8000

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

