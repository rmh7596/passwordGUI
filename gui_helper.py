# Simplified functions for use in the GUI
import random
import string
import rsa
import secure
import sqlite3
from entry import Entry # Class file

def generator(length):
    '''
    Password Generator
        Parameters:
            length (int): the length of the password to be generated
        Returns
            final (str): the generated password
    '''
    builder = []
    password = ""
    for i in range(length):
        char = random.choice(string.printable)              # Picks a random character from all printable chars in python
        if (char == " " or char == "\n" or char == "\t"):   # Filters out spaces, newlines, and tabs
            None
        else:
            builder.append(char)

    final = password.join(builder)
    return final

def store(website, usr, pswd):
    '''
    Stores information in a sql database
        Parameters:
            website (str): the website name
            usr (str): username
            pswd (str): password
        Returns:
            None
    '''
    s_pas = secure.encrypt(pswd.encode())
    connection = sqlite3.connect("data.db")     # Local database file name
    c = connection.cursor()
    
    try:
        c.execute('SELECT * FROM entry')
    except sqlite3.OperationalError:
        c.execute('''CREATE TABLE entry (website text, username text, password text)''')   
    
    c.execute("INSERT INTO entry VALUES (?,?,?)", (website, usr, s_pas))
    connection.commit() # Saves entry
    connection.close()


def retrieve_specific(name):
    '''
    Retrieves specific website name
        Parameters:
            name (str): Website name
        Returns:
            value (list): List containing the website name, username, and password
    '''
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute('SELECT * FROM entry WHERE website=?', (name,))
    value = c.fetchone()
    connection.close()
    d_value = (value[0], value[1], secure.decrypt(value[2]))
    return d_value

def retrieve_all():
    '''
    Retrieves all websites stored in the database
        Parameters:
            None
        Retuns:
            result (list): all the websites in the database
    '''
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute('SELECT website FROM entry')
    result = c.fetchall()
    connection.close()
    return result

    
