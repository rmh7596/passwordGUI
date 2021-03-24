# Plain text UI for password manager
import random
import rsa
import string
import sqlite3
from entry import Entry # Class file

publicKey, privateKey = rsa.newkeys(512)

def generator():
    '''
    Generates a random string
        Parameters:
            None
        Returns:
            None
    '''
    builder = []
    password = ""
    print("Please enter a password length:")
    length = int(input())
    for i in range(length):
        char = random.choice(string.printable)
        if (char == " " or char == "\n" or char == "\t"):
            None
        else:
            builder.append(char)

    final = password.join(builder)
    print("Your generated password is: " + final)
    print("Would you like to save that password?: Y/N")
    
    n = input()
    while(n != 'Y' and n != 'N'):
        print("Error: Wrong input")
    
    if (n == 'Y'):
        user = input("Please enter a username to be associated with the password:")
        site = input("Please enter the website that is associated with the entry:")
        store(site,user, final)
        
    if (n == 'N'):
        menu()


def encrypt(password):
    secure_pass =  rsa.encrypt(password.encode(), publicKey)
    return secure_pass;
    # decrypt d = rsa.decrypt(e, privateKey).decode()
    
def store(website, usr, pswd):
    '''
    Stores information in the databse
        Parameters:
            website (str): Website name
            usr (str): Username
            pswd (str): Password
        Returns:
            None
    '''
    e = Entry(website, usr, pswd)
    name = e.getUser()
    pas = e.getPass()
    web = e.getWeb()

    s_pass = encrypt(pas)
    print("Before: ", pas)
    print("After: ", s_pass)

    '''
    #Database
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute("INSERT INTO entry VALUES (?,?,?)", (web, name, pas))
    connection.commit()
    connection.close()
    menu()
    '''
    
    # Used once to create the table in the database
    #c.execute('''CREATE TABLE entry (website text, username text, password text)''')



def retrieve():
    '''
    Retrieves passwords from the database
        Parameters:
            None
        Returns:
            None
    '''
    print("Select Option:")
    print("1. Enter specific website for retrieval")
    print("2. Browse all saved passwords")
    print("3. Quit")
    q = input()
    
    while (True):
        if (q == '1' or q == '2' or q == '3'):
            break
        
        else:
            print("Error: Incorrect input. Please try again")
            q = input()

    if (q == '1'):
        w = input("Please enter the website name:")
        connection = sqlite3.connect("data.db")
        c = connection.cursor()
        c.execute('SELECT * FROM entry WHERE website=?', (w,))
        value = c.fetchone()
        print("Username: " + value[1])
        print("Password: " + value[2])
        connection.close()
        menu()


    if (q == '2'):
        connection = sqlite3.connect("data.db")
        c = connection.cursor()
        c.execute('SELECT website FROM entry')
        result = c.fetchall()
        print("Saved Websites:")
        for i in result:
            print(i[0], end =" ")
        print("\n")
        menu()

    if (q == '3'):
        print("Have a good day!")
        quit()

def menu():
    '''
    Redundant menu function
    '''
    print("What would you like to do?")
    print("1. Generate a password")
    print ("2. Store a password")
    print ("3. Retrieve a password")
    print("4. Quit")

    user =  input();

    while (True):
        if (user == '1' or user == '2' or user == '3' or user == '4'):
            break
        
        else:
            print("Error: Incorrect input. Please try again")
            user = input()

    if (user == '1'):
        generator()
    if (user == '2'):
        web = input("Enter Website:")
        u = input("Enter Username:")
        p = input("Enter Password:")
        print("Your password was stored")
        store(web, u, p)
    if (user == '3'):
        retrieve()
    if (user == '4'):
        print("Have a good day!")
        quit()

def main():
    '''
    Main driver function
        Parameters:
            None
        Retuns:
            None
    '''
    print("Welcome to my password manager!\nWhat would you like to do?")
    print("1. Generate a password")
    print ("2. Store a password")
    print ("3. Retrieve a password")
    print("4. Quit")

    user =  input();

    while (True):
        if (user == '1' or user == '2' or user == '3' or user == '4'):
            break
        
        else:
            print("Error: Incorrect input. Please try again")
            user = input()

    if (user == '1'):
        generator()
    if (user == '2'):
        web = input("Enter Website:")
        u = input("Enter Username:")
        p = input("Enter Password:")
        print("Your password was stored")
        store(web, u, p)
    if (user == '3'):
        retrieve()
    if (user == '4'):
        print("Have a good day!")
        quit()

if (__name__ == "__main__"):
    main()
