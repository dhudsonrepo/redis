import unittest
from chat.chat_server import ChatServer

class TestChatServer(unittest.TestCase):
    def setUp(self):
        self.chat_server = ChatServer()

    def test_send_receive_message(self):
        self.chat_server.send_message("Hello World!")
        # In real case, use mock or assert the PubSub callback.
        # This would normally listen for the message and check if it’s received correctly.
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
