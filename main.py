import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tabs.my_account import MyAccount
from tabs.chats import Chats
from components.account import Account

class MainWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title = "Tkinter Telegram"
        self.window.geometry("400x300")
        self.tabControl = ttk.Notebook(self.window)


        self.account = Account("estonya", APID, "API_HASH")
        self.me = self.account.get_me()

        self.tab1 = MyAccount(self.tabControl, self.me)
        self.tab2 = Chats(self.tabControl, self.account)

        self.tabControl.add(self.tab1.get_frame(), text ='Myaccount')
        self.tabControl.add(self.tab2.get_frame(), text ='Chats')
        self.tabControl.pack(expand = 1, fill ="both", padx=20, pady=20)

        self.window.mainloop()
        

MainWindow()