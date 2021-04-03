import sqlite3
import hashlib

def authenticate(username, password):
    '''
    Very basic login using predetermined username and password
        Parameters:
            username (str): inputted username
            password (str): inputted username
        Retuns:
            boolean
    '''

    connection = sqlite3.connect("data.db")     # Local database file name
    c = connection.cursor()
    
    try:
        c.execute('SELECT * FROM users')
    except sqlite3.OperationalError:
        c.execute('''CREATE TABLE users (username text, password text)''')   
    
    # Insert predetermined information
    hashed_pass = hashlib.sha256(b'Haver').hexdigest()
    c.execute("INSERT INTO users VALUES (?,?)", ("Ryan", hashed_pass))

    c.execute('SELECT * FROM users WHERE username=?', ("Ryan",))
    value = c.fetchone()
    
    connection.commit() # Saves entry
    connection.close()

    return (hashlib.sha256(password.encode()).hexdigest() == hashed_pass)
