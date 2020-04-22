import tsmail
import os_operations
import helpers
import exceptions
import validation
import requests
import json

from threading import Thread
from conf import config




#command handler
def command_handler(message,response_url):

    print(message)

    if not message:
        raise exceptions.FTPIncorrectSyntax("Empty String")
    
    command = message.split()[0]

    #CREATE
    if command == "create":

        folder, email =  validation.validate_create(message)
        return ftp_create_handler(folder, email)
    

    #DELETE
    elif command == "delete":
        #>Implement here
        pass
    else:
        raise exceptions.FTPIncorrectSyntax("Uknown command '" + command + "'")


#create handler
def ftp_create_handler(folder, email):

    #gerate random username
    username = helpers.generate_random_username()
    
    #generate ftp password
    password = helpers.generate_random_password()
    print(password)
    
    #create folder
    os_operations.create_folder(config.FOLDERS_PATH + folder)

    #create user
    os_operations.create_user(username, password, folder)

    #set owner
    os_operations.set_folder_owner(config.FOLDERS_PATH + folder, username)
    

    #SEND EMAIL
    #-----------------

    #set subject
    subject = config.EMAIL_SUBJECT

    #build email body
    body_str = open(config.HTML_TEMPLATE_LOCATION, "r").read()
    #replace servername token with sever IP
    body_str = body_str.replace(config.BODY_SERVER_TOKEN, config.SERVER_PUBLIC_IP)
    #replace foldername token with folder name
    body_str = body_str.replace(config.BODY_FOLDER_TOKEN,folder)
    #replace username token with generated username
    body_str = body_str.replace(config.BODY_USER_TOKEN, username)
    #replace password token with generated password
    body = body_str.replace(config.BODY_PASSWORD_TOKEN, password)

    #send confirmation email
    thr = Thread(target = tsmail.send_email, args=[email, subject, body])
    thr.start()

    return "Created FTP folder '" + folder + "'. Email will be sent to " + email