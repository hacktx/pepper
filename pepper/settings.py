import os

DEBUG = os.getenv('DEBUG') in ['True', 'true', '1', 'yes']
if DEBUG:
	SQLALCHEMY_ECHO = True

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

LOG_LEVEL = os.getenv('LOG_LEVEL') or 'debug'
SERVICE_NAME = os.getenv('SERVICE_NAME') or 'Nucelus'

SECRET_KEY = os.getenv('SECRET_KEY')
NONCE_SECRET = os.getenv('NONCE_SECRET')
HASHIDS_SALT = os.getenv('HASHIDS_SALT')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
HACKATHON_NAME = os.getenv('HACKATHON_NAME')
MLH_APPLICATION_ID = os.getenv('MLH_APPLICATION_ID')
MLH_SECRET = os.getenv('MLH_SECRET')
BASE_URL = os.getenv('BASE_URL')
GENERAL_INFO_EMAIL = os.getenv('GENERAL_INFO_EMAIL')
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
MAILGUN_PUB_KEY = os.getenv('MAILGUN_PUB_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')