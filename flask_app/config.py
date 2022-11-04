import json

# open config.json file
import os

with open("config.json") as config_file:
    config = json.load(config_file)


# Create a class for configuration

class Config:
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

    SECRET_KEY = config.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')
