from cache.redis_cache import RedisCache
from cache.disk_cache import DiskCache
from cache.remote_cache import RemoteCache

class CacheSystem:
    def __init__(self):
        self.redis_cache = RedisCache()
        self.disk_cache = DiskCache()
        self.remote_cache = RemoteCache()

    def get(self, key):
        # Try Redis cache first
        value = self.redis_cache.get(key)
        if value:
            return value

        # If not in Redis, try disk cache
        value = self.disk_cache.get(key)
        if value:
            return value

        # If not in disk cache, try remote cache
        value = self.remote_cache.get(key)
        if value:
            return value

        return None

    def set(self, key, value):
        # Set in Redis
        self.redis_cache.set(key, value)

        # Set in disk cache as well
        self.disk_cache.set(key, value)

        # Optionally set in remote cache
        self.remote_cache.set(key, value)

    def delete(self, key):
        self.redis_cache.delete(key)
        self.disk_cache.delete(key)
        self.remote_cache.delete(key)
