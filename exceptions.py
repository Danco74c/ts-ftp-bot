

#Parent Exception
class FTPException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'FTPIncorrectSyntax, {0} '.format(self.message)
        else:
            return 'FTPIncorrectSyntax has been raised'


# Incorrect syntax exception
class FTPIncorrectSyntax(FTPException):

    def __str__(self):
        if self.message:
            return 'FTPIncorrectSyntax, {0} '.format(self.message)
        else:
            return 'FTPIncorrectSyntax has been raised'

# Folder already exists expcetion
class FolderAlreadyExists(FTPException):

    def __str__(self):
        if self.message:
            return 'FolderExist, {0} '.format(self.message)
        else:
            return 'FolderAlreadyExists has being raised'

# Folder already exists expcetion
class FolderNotExist(FTPException):

    def __str__(self):
        if self.message:
            return 'FolderNotExist, {0} '.format(self.message)
        else:
            return 'FolderNotExist has being raised'


# User does not exist exception
class UserNotExist(FTPException):

    def __str__(self):
        if self.message:
            return 'UserNotExists, {0} '.format(self.message)
        else:
            return 'UserNotExists has being raised'

# User already exists
class UserAlreadyExist(FTPException):

    def __str__(self):
        if self.message:
            return 'UserAlreadyExist, {0} '.format(self.message)
        else:
            return 'UserAlreadyExist has being raised'

# Group does not exist exception
class GroupAlreadyExist(FTPException):

    def __str__(self):
        if self.message:
            return 'GroupAlreadyExist, {0} '.format(self.message)
        else:
            return 'GroupAlreadyExist has being raised'

# Group already exists exception
class GroupNotExist(FTPException):

    def __str__(self):
        if self.message:
            return 'GroupNotExist, {0} '.format(self.message)
        else:
            return 'GroupNotExist has being raised'