from pymongo import MongoClient

#Connection to MongoDB
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

#Setup database and collection
db = conn.voting_db
candidates_collection = db.candidates
votes = db.votes

#Candidate List
candidates_list = [ {"c_id":"1","name":"Mr. A"},
                    {"c_id":"2","name":"Mr. B"},
                    {"c_id":"3","name":"Miss C"} ]

#Insert candidates
for candidate in candidates_list:
    candidates_collection.insert(candidate)
    print("Candidate {0} wrote to MongoDB database".format(candidate["name"]))
