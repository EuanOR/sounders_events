from pymongo import MongoClient
# import pymongo
with open("db/mongo_connection.txt") as cs:
    CONNECTION_STRING = cs.readline().rstrip()

    client = MongoClient(CONNECTION_STRING)
    db = client['clickdimensions']
    events_collection = db['sounders_events']
def insert_events(events_data):
    
    events_collection.insert_one(events_data)

