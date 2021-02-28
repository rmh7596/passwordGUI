from tkinter import *
import auth
import gui_helper

def clear(func, l):
    '''
    Clears the window of all widgets 
        Parameters:
            func (function call): The function that is to be called after the window is cleared
            l (list): The list to clear
        Returns:
            None
        '''
    for i in l:
        i.pack_forget()
    func

def generator():
    '''
    Parent Function that generates passwords and saves them
        Parameters:
            None
        Returns:
            None
    '''

    g_wig = [] # Houses all the widgets
    
    def save(p):
        ''' 
        Takes a generated password and aquires more information and then saves it
            Parameters:
                p (str): The password generated 
            Returns:
                None
        '''
        clear(None, g_wig)
        u = StringVar()
        w = StringVar()
        
        l = Label(text="Please enter information to \n be associated with that password")
        l.pack(pady=3)
        g_wig.append(l)

        user = Label(text="Username:")
        user.pack()
        g_wig.append(user)

        user_e = Entry(textvariable = u)
        user_e.pack()
        g_wig.append(user_e)

        we = Label(text="Website:")
        we.pack()
        g_wig.append(we)


        web_e = Entry(textvariable = w)    
        web_e.pack()
        g_wig.append(web_e)


        submit = Button(text="Submit", command=lambda: gui_helper.store(w.get(),u.get(),p))
        submit.pack()
        g_wig.append(submit)


        back = Button(text="Back", command=lambda:  clear(manager(), g_wig))
        back.pack(side="bottom")
        g_wig.append(back)

    def gen(length):
        '''
        Password generator function that calls the helper function in gui_helper.py
        Uses try-except block to check for non-integer values entered    
            Parameters:
                length (str): The length of the password requested to be generated
            Returns:
                None
        '''
        try: 
            l = int(length) # Cast length to integer
            pswd = gui_helper.generator(l)
            g = Label(text="Your password is: " + pswd, pady=15)
            g.pack()
            g_wig.append(g)

            q = Label(text="Would you like to save that password?")
            q.pack()
            g_wig.append(q)

            yes = Button(text="Yes", command=lambda:save(pswd))
            yes.pack()
            g_wig.append(yes)
            
            no = Button(text="No")
            no.pack()
            g_wig.append(no)

        except ValueError:
            p.config(text="Please enter an integer value", fg="red")


    length_var = StringVar()
    p = Label(text="Enter a password length:")
    p.pack()
    g_wig.append(p)
    
    l = Entry(textvariable=length_var)
    l.pack()
    g_wig.append(l)

    b = Button(text="Submit", command=lambda: gen(length_var.get()))
    b.pack()
    g_wig.append(b)

    e = Button(text="Go back", command=lambda: clear(manager(), g_wig))
    e.pack(side="bottom")
    g_wig.append(e)

def store():
    '''
    Parent function for storing in a databse
        Parameters:
            None
        Returns:
            None
    '''

    s_wig = [] # Houses widgets
    
    u = StringVar()
    ps = StringVar()
    w = StringVar()

    user = Label(text="Username:")
    user.pack()
    s_wig.append(user)

    user_e = Entry(textvariable = u)
    user_e.pack()
    s_wig.append(user_e)

    p = Label(text="Password:")
    p.pack()
    s_wig.append(p)
    

    pe = Entry(textvariable = ps)
    pe.pack()
    s_wig.append(pe)

    we = Label(text="Website:")
    we.pack()
    s_wig.append(we)


    web_e = Entry(textvariable = w)    
    web_e.pack()
    s_wig.append(web_e)
    
    back = Button(text="Back", command=lambda: clear(manager(), s_wig))
    back.pack()
    s_wig.append(back)

    def submit():
        '''
        Calls the helper function in gui_helper to store the password in the database
            Parameter:
                None
            Returns:
                None
        '''
        gui_helper.store(w.get(),u.get(),ps.get())
        clear(None, s_wig)
        success = Label (text="Password was saved")
        success.pack()
        s_wig.append(success)
        back = Button(text="Back", command=lambda: clear(manager(), s_wig))
        back.pack()
        s_wig.append(back)

    
    sub  = Button(text="Submit",  command=submit)
    sub.pack(pady = 10)
    s_wig.append(sub)


def retrieve():
    '''
    Parent function to retrieve passwords
        Parameters:
            None
        Returns:
            None
    '''
    r_wig = [] # Houses widgets

    def get(name):
        '''
        Gets and displays the password from the database
            Parameters:
                name (str): The website name that the username and password is associated with
            Returns:
                None
        '''
        val = gui_helper.retrieve_specific(name)
        u = Label(text="Username: " + val[1])
        u.pack()
        r_wig.append(u)

        p = Label(text="Password: " + val[2])
        p.pack()
        r_wig.append(p)
        
        back = Button(text="Back", command=lambda: clear(manager(), r_wig))
        back.pack(side="bottom")
        r_wig.append(back)

    def specific():
        '''
        Gets the website name from input
            Paramters:
                None
            Returns:
                None
        '''
        clear(None, r_wig)
        w = Label(text="Website:")
        w.pack()
        r_wig.append(w)
        
        wv = StringVar()

        we = Entry(textvariable=w)
        we.pack()
        r_wig.append(we)

        sub  = Button(text="Submit", command=lambda: get(we.get()))
        sub.pack()
        r_wig.append(sub)

        back = Button(text="Back", command=lambda: clear(manager(), r_wig))
        back.pack()
        r_wig.append(back)



    specific = Button(text="Enter specific website for retrieval", command=specific)
    specific.pack()
    r_wig.append(specific)

    def general():
        '''
        Gets all the passwords stored in the database and displays them in a drop down menu
            Parameters:
                None
            Returns:
                None
        '''
        clear(None, r_wig)
        r = gui_helper.retrieve_all()
        var = StringVar()
        var.set(r[0])
        w = OptionMenu(master, var, *r)
        w.pack()
        r_wig.append(w)

        b = Button(text="Submit", command= lambda: get(var.get()[2:len(var.get())-3])) #Disgusting way of getting the name
        b.pack()
        r_wig.append(b)
           
    a = Button(text="Browse all saved passwords", command=general)
    a.pack()
    r_wig.append(a)


    back = Button(text="Back", command=lambda: clear(manager(), r_wig))
    back.pack(side="bottom")
    r_wig.append(back)

def manager():
    '''
    Main menu that displays the different options
        Parameters:
            None
        Returns:
            None
    '''
    
    m_widgets = [] # Houses the widgets

    label = Label(text="Password Manager:")
    label.pack()
    m_widgets.append(label)
               
    g = Button(text="Generate a password", command=lambda: clear(generator(), m_widgets))
    g.pack()
    m_widgets.append(g)
    s = Button(text="Store a password", command=lambda: clear(store(), m_widgets))
    s.pack()
    m_widgets.append(s)
    r = Button(text="Retrieve a password", command=lambda: clear(retrieve(), m_widgets))
    r.pack()       
    m_widgets.append(r)

    exit = Button(text="Exit", command=quit)
    exit.pack(side="bottom")
    m_widgets.append(exit)

'''
Presented Upon Launch
'''

widgets = [] #For login

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
    '''
    Verifies if the information inputted is the correct login, no sanitization yet
        Paramters:
            None
        Returns:
            None
    '''
    if auth.authenticate(uservar.get(), passvar.get()):
        clear(None, widgets)
        manager()
    else:
        label.config(text="Incorrect Password", fg='#f70000')
        

button1 = Button(text="Login", command= check)
button1.pack()
widgets.append(button1)


if __name__ == "__main__":
    mainloop()
