import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def square(x):
    print(f"Square function called with arg({x})")
    return x*x

square(256)
square(256)