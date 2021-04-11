# PasswordGUI
Simple password manager written in Python.

## Functions
1. Generate a password
  a. Gets an inputted length and returns a rnadom combination of letters and numbers
2. Store a password
  a. Takes a username, password, and website title, encrypts it, and stores it in a database
3. Retrieve a password
  a. Specific Website
    i. Takes a specific website name and retrieves it from the database
  b. All Websites
    i.  Fetches all website names from databse and puts them into a drop down menu
    ii. The credentials for the selected website is then outputted

## Libraries
1. Tkinter - One of Python's GUI libraries
2. RSA - Python's implemetation of the RSA system
3. SQLite3 - Python's interface for SQLite databases
4. Cryptography - Key generation and encryption

## Demonstration
![alt text](https://github.com/rmh7596/passwordGUI/blob/main/demonstration.gif)

## Project Status
4-11-2021

In its current state, the program only stores information for one user, me. In the future I would like to add the ability for multiple users. 
