import pymongo
client = pymongo.MongoClient("mongodb+srv://arup:Arup1234@cluster0.wztkw7o.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data = {
    "name":"Ineuron",
    "email" : "arup@ineuron.ai",
    "surname" : "kumar"
}

database = client['My_info']
collection = database['info']
collection.insert_one(data)