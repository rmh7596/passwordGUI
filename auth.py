def authenticate(username, password):
    '''
    Very, very basic login
        Parameters:
            username (str): inputted username
            password (str): inputted username
        Retuns:
            boolean
    '''
    if (username == "Ryan" and password == "Haver"):
        return True
    else:
        return False
