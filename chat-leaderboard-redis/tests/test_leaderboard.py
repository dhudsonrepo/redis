import unittest
from leaderboard.leaderboard import Leaderboard

class TestLeaderboard(unittest.TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard()

    def test_add_score(self):
        self.leaderboard.add_score("Alice", 100)
        self.leaderboard.add_score("Bob", 200)
        top_scores = self.leaderboard.get_top_scores(2)
        self.assertEqual(top_scores[0][0].decode('utf-8'), "Bob")
        self.assertEqual(top_scores[1][0].decode('utf-8'), "Alice")

    def test_get_user_score(self):
        self.leaderboard.add_score("Alice", 150)
        score = self.leaderboard.get_user_score("Alice")
        self.assertEqual(score, 150)

if __name__ == "__main__":
    unittest.main()
