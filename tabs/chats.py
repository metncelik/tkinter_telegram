from tkinter import ttk, messagebox
import tkinter as tk
from components.account import Account
from pyrogram.types.user_and_chats.dialog import Dialog

class Chats:
        def __init__(self, master, account: Account):
            self.master = master
            self.account = account
            self.frame = ttk.Frame(self.master,borderwidth=5)
            self.frame.columnconfigure(0, weight=1)
            self.frame.columnconfigure(1, weight=0)
            self.frame.rowconfigure(1, weight=1)
            self.dialogs = self.account.get_dialogs()

            self.combox = ttk.Combobox(self.frame)
            titles = list(self.dialogs.keys())
            self.combox["values"] = titles

            update_button = ttk.Button(self.frame, text="Get Messages", command=self.get_messages)
            self.lbox = tk.Listbox(self.frame)
            scroll = ttk.Scrollbar( self.frame, orient=tk.VERTICAL, command=self.lbox.yview)
            self.lbox.configure(yscrollcommand=scroll.set)


            update_button.grid(column=0, row=0, sticky="ne")
            self.lbox.grid(column=0, row=1, sticky="nwes")
            scroll.grid(column=1, row=1, sticky="ns")
            self.combox.grid(row=0,column=0, sticky="wn")
            self.lbox.activate(0)

        def get_messages(self):
             self.lbox.delete(0, tk.END)
             chat_title = self.combox.get()
             chat_id = self.dialogs[chat_title]
             messages = self.account.get_messages(chat_id)
             for index,message in enumerate(messages):
                self.lbox.insert(index, message)


        def get_frame(self):
            return self.frame