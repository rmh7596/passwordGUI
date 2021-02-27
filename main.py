from tkinter import *
import auth
import gui_helper

def generator():
    g_wig = []
    def clear(func):
        for i in g_wig:
            i.pack_forget()
        func

    def save(p):
        clear(None)
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


        back = Button(text="Back", command=lambda:  clear(manager()))
        back.pack(side="bottom")
        g_wig.append(back)

    def gen(length):
        try: 
            l = int(length)
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

    e = Button(text="Go back", command=lambda: clear(manager()))
    e.pack(side="bottom")
    g_wig.append(e)

def store():
    s_wig = []
    def clear(func):
        for i in s_wig:
            i.pack_forget()
        func
    
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

    def submit():
        gui_helper.store(w.get(),u.get(),ps.get())
        clear(None)
        success = Label (text="Password was saved")
        success.pack()
        s_wig.append(success)
        back = Button(text="Back", command=lambda: clear(manager()))
        back.pack()
        s_wig.append(back)

    
    sub  = Button(text="Submit",  command=submit)
    sub.pack(pady = 10)
    s_wig.append(sub)


def retrieve():
    r_wig = []
    def clear(func):
        for i in r_wig:
            i.pack_forget()
        func

    def get(name):
        val = gui_helper.retrieve_specific(name)
        u = Label(text="Username: " + val[1])
        u.pack()
        r_wig.append(u)

        p = Label(text="Password: " + val[2])
        p.pack()
        r_wig.append(p)
        
        back = Button(text="Back", command=lambda: clear(manager()))
        back.pack(side="bottom")
        r_wig.append(back)

    def specific():
        clear(None)
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



    specific = Button(text="Enter specific website for retrieval", command=specific)
    specific.pack()
    r_wig.append(specific)


    a = Button(text="Browse all saved passwords")
    a.pack()
    r_wig.append(a)


    back = Button(text="Back", command=lambda: clear(manager()))
    back.pack(side="bottom")
    r_wig.append(back)

def manager():
    m_widgets = []
    def clear(func):
        for i in m_widgets:
            i.pack_forget()
        func

    label = Label(text="Password Manager:")
    label.pack()
    m_widgets.append(label)
               
    g = Button(text="Generate a password", command=lambda: clear(generator()))
    g.pack()
    m_widgets.append(g)
    s = Button(text="Store a password", command=lambda: clear(store()))
    s.pack()
    m_widgets.append(s)
    r = Button(text="Retrieve a password", command=lambda: clear(retrieve()))
    r.pack()       
    m_widgets.append(r)

    exit = Button(text="Exit", command=quit)
    exit.pack(side="bottom")
    m_widgets.append(exit)


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
