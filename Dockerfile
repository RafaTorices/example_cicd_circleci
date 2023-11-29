# Image docker python base for flask app
FROM python:3.9
# Workdir default for aplication
WORKDIR /app
# Copy requirements.txt to container and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy all files to container
COPY src .
# Expose port 5000 for flask app
EXPOSE 5000
# Set environment variables
ENV FLASK_APP=calculator.py
# Run flask app
CMD ["flask", "run", "--host=0.0.0.0"]
