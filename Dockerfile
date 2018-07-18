FROM python:3.7.0-alpine

COPY . .

CMD [ "python3", "dht.py" ]
