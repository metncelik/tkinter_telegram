from tkinter import ttk, messagebox
from pyrogram.types.user_and_chats import User

class MyAccount:
        def __init__(self, master, me: User):
            self.master = master
            self.frame = ttk.Frame(self.master)
            self.frame.columnconfigure(0,weight=1)

            self.id = me.id
            self.name = me.first_name
            self.username = me.username
            self.phone = me.phone_number

            self.label1 = ttk.Label(self.frame, text="Id: ")
            self.label1.grid(row=0, column=0, sticky="w")
            self.label1 = ttk.Label(self.frame, text=self.id)
            self.label1.grid(row=0, column=1, sticky="e")

            self.label1 = ttk.Label(self.frame, text="Name: ")
            self.label1.grid(row=1, column=0, sticky="w")
            self.label1 = ttk.Label(self.frame, text=self.name)
            self.label1.grid(row=1, column=1, sticky="e")

            self.label1 = ttk.Label(self.frame, text="Username: ")
            self.label1.grid(row=2, column=0, sticky="w")
            self.label1 = ttk.Label(self.frame, text=self.username)
            self.label1.grid(row=2, column=1, sticky="e")

            self.label1 = ttk.Label(self.frame, text="Phone: ")
            self.label1.grid(row=3, column=0, sticky="w")
            self.label1 = ttk.Label(self.frame, text="+"+self.phone)
            self.label1.grid(row=3, column=1, sticky="e")

            self.frame.pack(expand=True,padx=20, pady=20)


        def get_frame(self):
            return self.frame