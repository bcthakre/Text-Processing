# USe a base image with Python 3.9-slim

FROM python:3.9-slim

# create a directory for our application

WORKDIR /app

# Copy Requirements and install dependecnies

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the python script to the container

COPY text-preprocessing.py .

# Run the script when the container starts

CMD ["python3", "./text-preprocessing.py"]