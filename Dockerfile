FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PRODUCTION True


RUN mkdir /config
RUN mkdir /src
ADD /config/requirements.txt /config/

RUN apk --no-cache add --virtual .build-deps gcc python3-dev musl-dev libc-dev make freetype-dev fribidi-dev \
    harfbuzz-dev jpeg-dev lcms2-dev openjpeg-dev tcl-dev tiff-dev tk-dev zlib-dev bash\
    && pip install --no-cache-dir -r /config/requirements.txt
    # && apk del .build-deps gcc libc-dev make

WORKDIR /src 