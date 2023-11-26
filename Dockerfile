FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the required files and directories into the container at /usr/src/app
COPY blog_app /usr/src/app/blog_app
COPY requirements.txt /usr/src/app

# Install dependencies
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# runs the server
ENTRYPOINT ["python", "blog_app/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
