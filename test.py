import secrets
import string
import os
from conf import config
from random_username.generate import generate_username



#create new folder
def create_folder(folder_path):

    #create folder if not already exists
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        os.chmod(folder_path, 0o666)

    else:
        raise FolderAlreadyExists(config.EXCP_MSG_FOLDER_EXSIST)

    return folder_path

create_folder("/home/FTPserver/dudu5")