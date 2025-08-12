import pymongo
my_clint=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=my_clint["mydatabase"]
mycol=mydb["mycollection"]
y={"name":"avinash","course":"python"}
x=mycol.insert_one(y)
