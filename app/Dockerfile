# pull official base image
FROM python:3.13.0rc1-slim-bookworm

# set work directory
WORKDIR /usr/src/app

# create directory for the app user
RUN mkdir -p /home/app
# RUN mkdir -p /usr/src/app/mediafiles
# RUN mkdir -p /usr/src/app/staticfiles


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]