import redis
from config.settings import REDIS_HOST, REDIS_PORT, REDIS_DB

class RedisCache:
    def __init__(self):
        self.client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value, ex=None):
        self.client.setex(key, ex, value) if ex else self.client.set(key, value)

    def delete(self, key):
        self.client.delete(key)
