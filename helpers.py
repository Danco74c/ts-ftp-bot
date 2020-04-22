import secrets
import string
from conf import config
from random_username.generate import generate_username


#create a random user name
def generate_random_username():
    return generate_username(config.SINGLE_USER)[0]


#generate a random password
def generate_random_password():
    
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(config.PASSWORD_LENGTH))
    return password