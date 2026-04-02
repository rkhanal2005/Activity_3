import tkinter as tk
from create_account import open_create_account
from timeout import start_timeout

def open_dashboard(username, role):

    root = tk.Tk()
    root.title("Dashboard")

    tk.Label(root, text=f"Welcome {username}").pack()

    if role == "manager":
        tk.Button(root, text="Create Account",
                  command=open_create_account).pack()

        tk.Label(root, text="Manager Dashboard").pack()

    else:
        tk.Label(root, text="Employee Dashboard").pack()

    start_timeout(root)

    root.mainloop()