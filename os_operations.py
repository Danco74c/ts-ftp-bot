import os
import pwd
import crypt
import grp
import shutil
from exceptions import *
from conf import config



#create new user
def create_user(name, password, home_folder):
    
    #check if FTP group exists
    out = os.system("sudo getent group " + config.FTP_GROUP_NAME)
    if out != 0:
        #create the ftp group
        os.system("sudo groupadd -g " + config.FTP_GROUP_ID + " " + config.FTP_GROUP_NAME)

    #check if user already exists
    out = os.system("id -u " + name)
    if out == 0:
        raise UserAlreadyExist(config.EXCP_MSG_USER_EXSIST)

    encPass = crypt.crypt(password,"22")

    #create user
    os.system("sudo useradd -p " + encPass +  " -d " + config.FOLDERS_PATH + home_folder + " " + name + " -g " + config.FTP_GROUP_NAME)
    return pwd.getpwnam(name)


#delete user
def delete_user(name):
    #delete user
    os.system("sudo userdel -r " + name)


#create new folder
def create_folder(folder_path):

    #create folder if not already exists
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        os.chmod(folder_path, config.FOLDER_PERMISSION)
        #create uploads folder
        os.mkdir(folder_path + config.UPLOAD_FOLDER_NAME)
        os.chmod(folder_path, config.UPLOAD_FOLDER_NAME)

    else:
        raise FolderAlreadyExists(config.EXCP_MSG_FOLDER_EXSIST)

    return folder_path


#delete folder
def delete_folder(folder_path):
    #check if folder exists
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path, True)

#list folder
def get_folder_content(folder_path):
    #check if folder exists
    if os.path.exists(folder_path):
        return os.listdir(folder_path)


#set folder owner
def set_folder_owner(folder_path, owner):

    #check if user exist
    try:
        uid = pwd.getpwnam(owner).pw_uid
    except KeyError:
        raise UserNotExist(config.EXCP_MSG_USER_NOT_EXSIST)

    #check if group exist
    try:
        gid = grp.getgrnam(config.ADMIN_GROUP_NAME).gr_gid
    except KeyError:
        raise GroupNotExist(config.EXCP_MSG_GROUP_NOT_EXSIST)

    #check if folder exist
    if not os.path.exists(folder_path):
        raise FolderNotExist(config.EXCP_MSG_FOLDER_NOT_EXSIST)
    print("folder:" + folder_path + " uid: " + str(uid) + " gid: " + str(gid))
    os.chown(folder_path, uid, gid)

    
