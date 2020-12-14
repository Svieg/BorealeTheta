# Pull base image.
FROM ubuntu:18.04

# Install.
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget netcat python3 python3-pip && \
  rm -rf /var/lib/apt/lists/* \
  pip3 install requests \
  pip3 install flask

# Add files.
ADD . / ./
# Define default command.
ENV FLASK_APP ui.py 
CMD ["flask run --host 0.0.0.0 --port 5000"]
