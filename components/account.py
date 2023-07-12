from pyrogram import Client
from pyrogram.types.user_and_chats.chat import Chat

class Account:
        def __init__(self, name: str, api_id: int, api_hash: str):
            self.client = Client(name, api_id, api_hash,)
            self.client.start()
        
        def get_me(self):
             me = self.client.get_me()
             return me
        
        def get_dialogs(self):
            dialogs_asdict = {}
            dialogs = self.client.get_dialogs()
            for dialog in dialogs:
                 chat = dialog.chat
                 dialogs_asdict[chat.first_name] = chat.id
            return dialogs_asdict
        
        def get_messages(self, id:int or str):
             messages = self.client.get_chat_history(id)
             texts = []
             for message in messages:
                  texts.append(f"{message.from_user.first_name}: {message.text}")
             return texts