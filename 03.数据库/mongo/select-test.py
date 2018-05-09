from pymongo import MongoClient

client = MongoClient()
db = client.stock
cursor = db.stock_rank.find()

for data in cursor:
    print data
    break