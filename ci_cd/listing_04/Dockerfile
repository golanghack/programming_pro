FROM jenkins/jenkins:lts
USER root 
RUN apt update
RUN apt install python3.9 -y
RUN apt install python3-pip -y
RUN  rm -rf /var/lib/apt/lists/*
RUN pip install tox 
