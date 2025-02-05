import os
import pickle
from config.settings import DISK_CACHE_DIR

class DiskCache:
    def __init__(self):
        if not os.path.exists(DISK_CACHE_DIR):
            os.makedirs(DISK_CACHE_DIR)

    def _get_disk_cache_path(self, key):
        return os.path.join(DISK_CACHE_DIR, f"{key}.pkl")

    def get(self, key):
        cache_path = self._get_disk_cache_path(key)
        if os.path.exists(cache_path):
            with open(cache_path, 'rb') as f:
                return pickle.load(f)
        return None

    def set(self, key, value):
        cache_path = self._get_disk_cache_path(key)
        with open(cache_path, 'wb') as f:
            pickle.dump(value, f)

    def delete(self, key):
        cache_path = self._get_disk_cache_path(key)
        if os.path.exists(cache_path):
            os.remove(cache_path)
