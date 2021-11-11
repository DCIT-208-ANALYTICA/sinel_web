# pull official base image
FROM python:3.9.6-alpine

# create directory for the app user
RUN mkdir -p /home/sinel_web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the appropriate directories
ENV HOME=/home/sinel_web
ENV APP_HOME=/home/sinel_web/app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME


# install dependencies
RUN apk update \
    # && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && apk add openssl-dev libffi-dev \
    && apk add jpeg-dev zlib-dev libjpeg

RUN pip install --upgrade pip

COPY ./requirements.txt $APP_HOME
RUN pip install -r requirements.txt

# Delet temp build dir.
# RUN apk del build-deps

COPY ./entrypoint.sh $APP_HOME
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

# chown all the files to the app user
RUN chown -R sinel_web:sinel_web $APP_HOME

# copy project
COPY . $APP_HOME

# run entrypoint.sh
ENTRYPOINT ["/home/sinel_web/app/entrypoint.sh"]
