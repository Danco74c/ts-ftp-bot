import requests
import json
import string
import secrets

from conf import config


requests.packages.urllib3.disable_warnings()  # Ignore from requests module warnings

def pass_gen():
    # Generate password for new sftp user
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    return password


# Perform a request to API gateway which trigger 'FTPserver' lambda function
def create_ftp_folder(company, password):
    url = config.SFTP_URL
    data = {"company": company, "password": password}
    headers = []
    response = requests.request("POST", url, data=json.dumps(data), headers=headers, verify=False)


# Perform a request to API gateway which trigger 'auto_mail' lambda function
def send_email(recipient, subject, body):
    body = open("html/confirmation_email.html", "r").read()
    url = config.EMAIL_URL
    data = {"recipient": recipient, "subject": "FTP Confirmation", "body": body}
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, data=json.dumps(data), headers=headers, verify=False)
    return response.text


#< Send slack incoming WebHook to 'prj-ts_ftp' channel
#def send_slack_message(text):
#    print(text)
#    url = config.SLACK_URL
#    payload = {"text": text}
#    headers = {'Content-Type': "application/json"}
#    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
