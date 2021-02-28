# Entry Class
class Entry():
    '''
    A class to represent an entry in the database

    Attributes
    ----------
    website : str
        Website name
    username : str
        Username
    password : str
        Password

    Methods
    -------
    getUser
        Getter
    getPass
        Getter
    getWeb
        Getter
    '''

    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def getUser(self):
        '''
        Gets the username
            Parameters:
                self
            Returns:
                Username
        '''
        return self.username

    def getPass(self):
        '''
        Gets the password
            Parameters:
                self
            Returns:
                password
        '''
        return self.password

    def getWeb(self):
        '''
        Gets the website name
            Parameters:
                self
            Retuns
                website
        '''
        return self.website

