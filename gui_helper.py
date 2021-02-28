# Simplified functions for use in the GUI
import random
import string
import sqlite3
from entry import Entry # Class file


def generator(length):
    builder = []
    password = ""
    for i in range(length):
        char = random.choice(string.printable)
        if (char == " " or char == "\n" or char == "\t"):
            None
        else:
            builder.append(char)

    final = password.join(builder)
    return final


def store(website, usr, pswd):
    #Database
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    #c.execute('''CREATE TABLE entry (website text, username text, password text)''')
    c.execute("INSERT INTO entry VALUES (?,?,?)", (website, usr, pswd))
    connection.commit()
    connection.close()


def retrieve_specific(name):
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute('SELECT * FROM entry WHERE website=?', (name,))
    value = c.fetchone()
    connection.close()
    return value

def retrieve_all():
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute('SELECT website FROM entry')
    result = c.fetchall()
    connection.close()
    return result

    
