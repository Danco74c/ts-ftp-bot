from operations import create_ftp_folder, send_email, pass_gen
from exceptions import FTPIncorrectSyntax
from validation import validate_create
from threading import Thread
from conf import config
import requests
import json

#command handler
def command_handler(message,response_url):

    print(message)

    if not message:
        raise FTPIncorrectSyntax("Empty String")
    
    command = message.split()[0]

    #CREATE
    if command == "create":

        folder, email =  validate_create(message)
        thr = Thread(target=ftp_create_handler, args=[folder,email,response_url])
        thr.start()
        return "Creating FTP folder '" + folder + "'. Email will be sent to " + email

    #DELETE
    elif command == "delete":
        #>Implement here
        pass
    else:
        raise FTPIncorrectSyntax("Uknown command '" + command + "'")


#create handler
def ftp_create_handler(folder, email, response_url):

    #generate ftp password
    password = pass_gen()
    #>add validation here
    print(create_ftp_folder(folder, password))
    print(send_email(email, folder, password))
    
    payload = {"text":"your task is complete"}
    requests.post(response_url,data=json.dumps(payload))