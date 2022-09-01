import pymongo
client = pymongo.MongoClient("mongodb+srv://arup:Arup1234@cluster0.wztkw7o.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Arup",
    "email" : "arup@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['test']
coll = db1['test']
coll.insert_one(d)