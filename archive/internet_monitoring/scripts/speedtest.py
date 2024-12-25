#!/usr/bin/env python3

import csv
import datetime
import subprocess


def measure_speed():
    result = subprocess.run(['speedtest-cli', '--simple'], capture_output=True, text=True)
    if result.returncode == 1:
        print(f"==> {result.stdout}")
    output = result.stdout
    download_speed = 0
    upload_speed = 0
    ping = 0
    for line in output.split('\n'):
        if 'Download' in line:
            download_speed = line.split()[1]
        if 'Upload' in line:
            upload_speed = line.split()[1]
        if 'Ping' in line:
            ping = int(float(line.split()[1]))
    return download_speed, upload_speed, ping


def log_speed_to_csv(now, filename, download_speed, upload_speed, ping):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([now, download_speed, upload_speed, ping])


def main():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    filename = 'speed.csv'
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csvwriter.writerow(['datetime', 'download_speed', 'upload_speed', 'ping'])
    download_speed, upload_speed, ping = measure_speed()
    log_speed_to_csv(now, filename, download_speed, upload_speed, ping)

if __name__ == '__main__':
    main()
