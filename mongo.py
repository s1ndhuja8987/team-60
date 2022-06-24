import pymongo

def signup(name, userID, pwd, email):
    new={"User ID":userID, "Email":email, "Password":pwd, "Name":name}
    collection.insert_one(new)

def fetch(userID):
    match=collection.find_one({"User ID":userID}, {"User ID":1, "Password":1, "_id":0})
    return(match)

def reset(userID, new_pwd):
    prev={"User ID":userID}
    nxt={"$set":{"Password":new_pwd}}
    collection.update_one(prev,nxt)

def delete(userID):
    collection.delete_one({"User ID":userID})

if __name__=="__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    db=client['Team_60']
    collection=db['Credentials']
    signup("akc","akc123","1234","asd@asd")
    print("Created")
    print(fetch("akc123"))
    reset("akc123", "7894")
    print(fetch("akc123"))
    delete("akc123")