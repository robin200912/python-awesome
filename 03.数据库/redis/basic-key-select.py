from redis import Redis
# from redis import StrictRedis

redis = Redis()
redis.set('name', 'robin')

print redis.get('name')

