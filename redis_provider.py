import redis
import datetime

MESSAGES_KEY = "messages"


def extract_message(value):
    return {
        "content": value[0].decode("utf-8").split(":")[0],
        "timestamp": value[1]
    }


class RedisProvider():
    def __init__(self, host, port):
        self.r = redis.Redis(host=host, port=port, db=0)

    def publish(self, content):
        current_timestamp = datetime.datetime.utcnow().timestamp()
        self.r.zadd(MESSAGES_KEY, {content + ":" + str(current_timestamp): current_timestamp})

    def get_last(self):
        res = self.r.zrange(MESSAGES_KEY, -1, -1, withscores=True)
        if not res:
            return "", 204
        return extract_message(res[0])

    def get_by_time(self, start="-inf", end="inf"):
        res = self.r.zrangebyscore(MESSAGES_KEY, start, end, withscores=True)
        return list(map(extract_message, res))


