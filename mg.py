import json
from pymongo import MongoClient

mg_client = MongoClient('mongodb+srv://igorrrockit:l1ZNpEnUtZzHaYuR@cluster0.g81yooe.mongodb.net/?retryWrites=true&w=majority')
mydb = mg_client["my_db"]
my_col = mydb["rus_losses"]

# path = '/home/ihor.tymoshenko/Levi9PythonMeetup/frameworks/casualities.json'
# with open(path) as f:
#     content = json.load(f)
#     x = my_col.insert_many(content)
#     print(len(x.inserted_ids), '******')
print(mydb.list_collection_names(), mg_client.list_database_names())
print([i for i in map(lambda x: type(x['_id']), my_col.find(limit=50))])