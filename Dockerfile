FROM python:3.8.5-alpine3.12

WORKDIR /app

RUN pip install requests

ADD service.py /app

CMD [ "python", "/app/service.py" ]
