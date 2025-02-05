import requests
from config.settings import REMOTE_CACHE_URL

class RemoteCache:
    def __init__(self):
        self.url = REMOTE_CACHE_URL

    def get(self, key):
        response = requests.get(f"{self.url}/get/{key}")
        if response.status_code == 200:
            return response.json().get('value')
        return None

    def set(self, key, value):
        response = requests.post(f"{self.url}/set", json={'key': key, 'value': value})
        return response.status_code == 200

    def delete(self, key):
        response = requests.delete(f"{self.url}/delete/{key}")
        return response.status_code == 200
