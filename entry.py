# Entry Class
class Entry():
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def getUser(self):
        return self.username

    def getPass(self):
        return self.password

    def getWeb(self):
        return self.website
