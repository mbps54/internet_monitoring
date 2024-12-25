#!/usr/bin/env python3

import csv
import datetime
import subprocess
import re


def log_speed_to_csv(now, filename, ping, delay):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([now, ping, delay])

def ping_ip(ip):
    result = 0
    ping_result = subprocess.run(['ping', '-c', '2', '-n', '-W', '2', ip],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    encoding='utf-8')
    if ping_result.returncode == 0:
        result = 1
    return(result)

def ping_delay(ip):
    try:
        # Run the ping command and capture the output
        ping_result = subprocess.run(
            ['ping', '-c', '2', '-n', '-W', '2', ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8'
        )
        # Check if the ping command was successful
        if ping_result.returncode == 0:
            # Extract the average delay from the ping output
            output = ping_result.stdout
            # Use regex to find the average time in the output
            match = re.search(r'time=([0-9.]+) ms', output)
            if match:
                delay = int(round(float(match.group(1)), 0))
                return delay
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    filename = '/home/admin/ping.csv'
    ip = '9.9.9.9'
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csvwriter.writerow(['datetime', 'ping', 'delay'])
    ping = ping_ip(ip)
    delay = ping_delay(ip)
    log_speed_to_csv(now, filename, ping, delay)

if __name__ == '__main__':
    main()

