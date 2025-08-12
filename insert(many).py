import pymongo
myclint=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclint["Avi"]
mycol=mydb["login"]
mylist=[
    {"name":"Arun","course":"Aiml"},
    {"name":"Avinash","course":"Aiml"},
    {"name":"sabura","course":"Anesthesiology"}
    ]
x=mycol.insert_many(mylist)
print(x.inserted_ids)