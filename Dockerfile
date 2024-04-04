FROM python:3.11-slim
#Todo: move this part to separete image as base image #####>
RUN apt-get update && apt-get install -y --no-install-recommends
RUN apt-get install -y wget gnupg
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \ 
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable
#<########### 
#RUN pip install selenium behave

WORKDIR /app

COPY ./features ./features
COPY ./behave.ini ./behave.ini
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD [ "behave" ]
