import tkinter as tk
from tkinter import messagebox
from database import verify_user, get_all_usernames
from dashboard import open_dashboard

class LoginWindow:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Store Login")

        tk.Label(self.root, text="Username").pack()
        self.username = tk.Entry(self.root)
        self.username.pack()

        tk.Label(self.root, text="Password").pack()
        self.password = tk.Entry(self.root, show="*")
        self.password.pack()

        tk.Button(self.root, text="Login",
                  command=self.login).pack()

        self.root.mainloop()

    def login(self):

        user = self.username.get()
        pw = self.password.get()

        role = verify_user(user, pw)

        if role:
            self.root.destroy()
            open_dashboard(user, role)

        else:
            messagebox.showerror("Error", "Invalid login")