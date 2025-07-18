FROM python:3.13-alpine

RUN pip install requests==2.28.2 && pip install python-telegram-bot==13.15 && pip install standard-imghdr 

WORKDIR /opt/weatherbot

COPY run.py /opt/weatherbot

CMD ["python", "run.py"]
