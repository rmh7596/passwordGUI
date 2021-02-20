# Plain text UI for password manager
import random
import string


def generator():
    builder = []
    password = ""
    print("Please enter a password length:")
    length = input()
    for i in range(length):
        char = random.choice(string.printable)
        if (char == " " or char == "\n" or char == "\t"):
            None
        else:
            builder.append(char)

    final = password.join(builder)
    print("Your generated password is: " + final)
    print("Would you like to save that password?: Y/N")
    
    n = raw_input()
    while(n != 'Y' and n != 'N'):
        print("Error: Wrong input")
    
    if (n == 'Y'):
        user = raw_input("Please enter a username to be associated with the password:")
        store(user, final)
        
    if (n == 'N'):
        menu()

def store(usr, pswd):
    print(usr + " " + pswd)

def retrieve():
    None

def menu():
    print("What would you like to do?")
    print("1. Generate a password")
    print ("2. Store a password")
    print ("3. Retrieve a password")
    print("4. Quit")

    user =  raw_input();

    while (True):
        if (user == '1' or user == '2' or user == '3' or user == '4'):
            break
        
        else:
            print("Error: Incorrect input. Please try again")
            user = raw_input()

    if (user == '1'):
        generator()
    if (user == '2'):
        store()
    if (user == '3'):
        retrieve()
    if (user == '4'):
        print("Have a good day!")
        quit()

def main():
    print("Welcome to my password manager!\nWhat would you like to do?")
    print("1. Generate a password")
    print ("2. Store a password")
    print ("3. Retrieve a password")
    print("4. Quit")

    user =  raw_input();

    while (True):
        if (user == '1' or user == '2' or user == '3' or user == '4'):
            break
        
        else:
            print("Error: Incorrect input. Please try again")
            user = raw_input()

    if (user == '1'):
        generator()
    if (user == '2'):
        store()
    if (user == '3'):
        retrieve()
    if (user == '4'):
        print("Have a good day!")
        quit()

if (__name__ == "__main__"):
    main()
