from validate_email import validate_email
from exceptions import FTPIncorrectSyntax
import re
import config


# parse message
def validate_create(msg):
    print("Validating create message")
    # split the message and ensure correct number of arguments
    split_command = msg.split()
    if not len(split_command) == config.CREATE_NUMBER_OF_ARGUMENTS:
        raise FTPIncorrectSyntax("Incorrect number of arguments for create")
    folder = split_command[1]
    email = split_command[2]


    # validate folder
    if not validate_folder(folder):
        raise FTPIncorrectSyntax("Folder name must be between 3 and 20 valid characters")

    #validate email
    if not validate_email(email):
        raise FTPIncorrectSyntax("Invalid email address")


    #on sucessful validation return folder and email
    return folder, email


def validate_folder(folder):
    print(folder)
    #validate folder
    folderPattern = re.compile("[A-Za-z0-9\-\_]{3,20}")
    if not folderPattern.fullmatch(folder):
        return False
    return True
