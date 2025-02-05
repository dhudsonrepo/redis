import unittest
from main import CacheSystem

class TestCacheSystem(unittest.TestCase):
    def setUp(self):
        self.cache = CacheSystem()

    def test_cache_get_set(self):
        self.cache.set("user:123", "John Doe")
        result = self.cache.get("user:123")
        self.assertEqual(result, "John Doe")

    def test_cache_delete(self):
        self.cache.set("user:123", "John Doe")
        self.cache.delete("user:123")
        result = self.cache.get("user:123")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
