from chat.chat_server import ChatServer

class ChatClient:
    def __init__(self, username):
        self.username = username
        self.server = ChatServer()

    def send_message(self, message):
        full_message = f"{self.username}: {message}"
        self.server.send_message(full_message)

    def listen_for_messages(self):
        self.server.listen_for_messages()
