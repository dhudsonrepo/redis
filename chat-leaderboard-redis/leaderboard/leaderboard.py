import redis
from config.settings import REDIS_HOST, REDIS_PORT, REDIS_DB, LEADERBOARD_KEY

class Leaderboard:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    def add_score(self, username, score):
        self.redis_client.zadd(LEADERBOARD_KEY, {username: score})

    def get_top_scores(self, top_n=10):
        return self.redis_client.zrevrange(LEADERBOARD_KEY, 0, top_n-1, withscores=True)

    def get_user_score(self, username):
        return self.redis_client.zscore(LEADERBOARD_KEY, username)

    def reset_leaderboard(self):
        self.redis_client.delete(LEADERBOARD_KEY)
