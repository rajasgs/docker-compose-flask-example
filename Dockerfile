# Use the LTS release.
FROM python:2.7

RUN useradd --user-group --create-home --shell /bin/false app 
  
ENV HOME=/home/app

USER app
WORKDIR $HOME/api_sample
