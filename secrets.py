import os

class Constants:
    WEBHOOK = (
	    os.environ.get('SLACK_INCOMING_WEBHOOK')
    )
    DB_HOST = os.environ.get('DB_HOST')
    DB_USER = os.environ.get('DB_USER')
    DB_PWD = os.environ.get('DB_PASSWD')
    DB_NAME = os.environ.get('DB_NAME')
    if os.environ.get('OVERFLOW_THRESHOLD'):
        THRESHOLD = os.environ.get('OVERFLOW_THRESHOLD')
    else:
        THRESHOLD = 90
