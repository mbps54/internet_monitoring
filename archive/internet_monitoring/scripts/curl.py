#!/usr/bin/env python3

import csv
import datetime
import subprocess
import click


def log_speed_to_csv(now, filename, curl):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([now, curl])


def curl(url):
    result = 0
    curl_result = subprocess.run(['curl', url],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    encoding='utf-8')
    if curl_result.returncode == 0:
        result = 1
    return(result)


@click.command()
@click.option('--url', default='https://binicivadi.com', help='URL to fetch')
def main(url):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    filename = 'curl.csv'
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csvwriter.writerow(['datetime', 'curl'])
    result = curl(url)
    log_speed_to_csv(now, filename, result)

if __name__ == '__main__':
    main()
