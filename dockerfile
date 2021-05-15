FROM python:alpine
WORKDIR /src
COPY src/app.py /src/app.py
CMD python /src/app.py