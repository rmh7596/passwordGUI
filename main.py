from tkinter import *
import auth
import ptui

def manager():
    label = Label(text="Password Manager:")
    label.pack()
               
    g = Button(text="Generate a password")
    g.pack()
    s = Button(text="Store a password")
    s.pack()
    r = Button(text="Retrieve a password")
    r.pack()       


def clearLogin(w):
    for i in w:
        i.pack_forget()


widgets = []

master = Tk()
master.title("Password Manager")
master.geometry("250x250")


label = Label(text="Password Manager")
label.pack(side="top")
widgets.append(label)
uservar = StringVar()
passvar = StringVar()
    
user = Label(text="Username:")
user.pack()
widgets.append(user)

user_e = Entry(textvariable = uservar)
user_e.pack()
widgets.append(user_e)

p = Label(text="Password:")
p.pack()
widgets.append(p)


pass_e = Entry(textvariable = passvar, show="*")    
pass_e.pack()
widgets.append(pass_e)

        
def check():
    if auth.authenticate(uservar.get(), passvar.get()):
        clearLogin(widgets)
        manager()
    else:
        label.config(text="Incorrect Password", fg='#f70000')
        

button1 = Button(text="Login", command= check)
button1.pack()
widgets.append(button1)


if __name__ == "__main__":
    mainloop()
