import requests
import json
import string
import secrets

from conf import config


requests.packages.urllib3.disable_warnings()  # Ignore from requests module warnings


# Perform a request to API gateway which trigger 'auto_mail' lambda function
def send_email(recipient, subject, body):
    url = config.EMAIL_URL
    data = {"recipient": recipient, "subject": subject, "body": body}
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, data=json.dumps(data), headers=headers, verify=False)
    return response.text