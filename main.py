import tkinter as tk
import ptui

root = tk.Tk()
root.title("Password Manager")
#root.geometry("300x500")

u = tk.Label(root, text="Username:")
u.grid(row=0, column=0, pady=5, padx = 25)
p = tk.Label(root, text="Password:")
p.grid(row=1, column=0, pady=5, padx = 25)

u_entry = tk.Entry(root)
u_entry.grid(row=0, column=1)

p_entry = tk.Entry(root)
p_entry.grid(row=1, column=1)

login = tk.Button(root, text="Login", padx = 15, command=ptui.generator)
login.grid(row=0, column=2)

root.mainloop()
