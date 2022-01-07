FROM python:2
ENV PYTHONUNBUFFERED=1
WORKDIR /mysite/
COPY require.txt /mysite/
RUN apt-get install libjpeg62-turbo-dev libtiff-dev
RUN pip install -r require.txt
COPY mysite/ /mysite/
# EXPOSE 9000
WORKDIR /mysite/