from pymongo import MongoClient

client = MongoClient("mongodb+srv://hugogarsan:Monlau2021@cluster0.tbqe7bk.mongodb.net/")

db = client.BeatNow

collectionUsers = db["Users"]

