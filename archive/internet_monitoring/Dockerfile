FROM python:3.9-slim

WORKDIR /home/admin

COPY ./scripts/ /home/admin

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y cron speedtest-cli

COPY crontab /etc/cron.d/scheduler

RUN chmod 0644 /etc/cron.d/scheduler

RUN crontab /etc/cron.d/scheduler

CMD cron
