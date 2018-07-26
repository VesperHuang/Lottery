from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("mongodb://127.0.0.1:27017")
db = conn.runoob
collection = db.teachers

#collection.stats # 如果沒有error，你就連線成功了
#find
#cursor = collection.find_one({'_id':ObjectId("5b57eeeecd5b9516bb70cdf0")})

#cursor = collection.find()
#data = [d for d in cursor] # 這樣才能真正從資料庫把資料庫撈到python的暫存記憶體中
#print(data)


#delete
# 刪除一筆資料
#collection.delete_one({'_id':ObjectId("5b57eeeecd5b9516bb70cdf0")})

# 刪除全部資料
#collection.delete_many({})

# 刪除多筆資料
#collection.delete_many({'<column_name>': '<what_you_want>'})

#insert
# 插入一筆資料: 請放入一個dict
#collection.insert_one({"name":"vesper_huang","age":"28"})

# 插入多筆資料: 請放入一個dist
#collection.insert_many(<to_be_insert_dist>)

#update
#collection.update_one({"_id" : ObjectId("5b59d0d361ae0e076a8415fe")},{'$set':{'age':'38'}})



