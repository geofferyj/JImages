FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PRODUCTION True
ENV GUNICORN_CONF /config/gunicorn_conf.py

RUN mkdir /config
ADD /config/requirements.txt /config/
ADD /config/gunicorn_conf.py /config/

RUN apk --no-cache add --virtual harfbuzz-dev jpeg-dev lcms2-dev build-base openjpeg-dev tcl-dev tiff-dev tk-dev zlib-dev
    
RUN pip install --no-cache-dir -r /config/requirements.txt

COPY ./project /app
WORKDIR /app