import os
import sys
import logging

def monitor_logs(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO)

    try:
        with open(log_file, 'r') as file:
            logs = file.read()
    except Exception as e:
        logging.error("Failed to read log file: %s", str(e))
        sys.exit(1)

    suspicious_activities = ['unauthorized', 'failed login', 'access denied', 'error']

    for activity in suspicious_activities:
        if activity in logs:
            logging.warning("Suspicious activity detected: %s", activity)

if __name__ == "__main__":
    log_file = '/path/to/your/log/file'
    monitor_logs(log_file)