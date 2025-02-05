import redis
from config.settings import REDIS_HOST, REDIS_PORT, REDIS_DB, CHAT_CHANNEL

class ChatServer:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        self.pubsub = self.redis_client.pubsub()
        self.pubsub.subscribe(CHAT_CHANNEL)

    def send_message(self, message):
        self.redis_client.publish(CHAT_CHANNEL, message)

    def listen_for_messages(self):
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                print(f"New message: {message['data'].decode('utf-8')}")
