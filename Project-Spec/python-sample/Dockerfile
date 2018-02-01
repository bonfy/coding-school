# Use an official Python runtime as a parent image
FROM python:latest

# 设置VOLUME
VOLUME ["/config", "/log"]

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# 设置时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r req.txt

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
# ENV NAME World

# Run app.py when the container launches

# CMD 固定命令， 不能传参数
# CMD ["python", "app.py"]

ENTRYPOINT ["python", "app.py"]