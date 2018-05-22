
# Q3a - Simple Voting System API Design

## 1. Tools
* Database - MongoDB
* Python 3
    * PyMongo
    * Flask
* Postman

## 2. Environment Setup

* Virtual Environment

1. Install virtualenv
2. Create virtual environment
3. Activate virtual environment

```console
$ pip install virtualenv
```
```console
$ python3.6 -m venv env
```
```console
$ source env/bin/activate
```
* Install Flask
```console
$ pip install Flask
```
* Install Pymongo
```console
$ python -m pip install pymongo
```
## 3. Database Setup

* Run create_db.py to create database
```console
$ python create_db.py
```
* Connect MongoDB
```console
#Connection to MongoDB
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")
```

* Create database and collection
```console
db = conn.voting_db
candidates_collection = db.candidates
votes = db.votes

candidates_list = [ {"c_id":"1","name":"Mr. A"},
                    {"c_id":"2","name":"Mr. B"},
                    {"c_id":"3","name":"Miss C"} ]
```

* Insert candidates
```console
for candidate in candidates_list:
    candidates_collection.insert(candidate)
    print("Candidate {0} wrote to MongoDB database".format(candidate["name"]))
```
## 4. Deisgn API Endpoints

1. GET - @app.route('/result') - Display candidate result 
2. POST - @app.route('/vote/<string:c_id>') - Vote individual candidate

* Setting up configuration
```console
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'voting_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/voting_db'
mongo = PyMongo(app)
```
* API Endpoints

    1. GET - @app.route('/result') - Display candidate result
```console
@app.route('/result')
def get_result():
    candidates = mongo.db.candidates
    votes = mongo.db.votes
    candidates_result = []
    last_10m = datetime.datetime.now() - datetime.timedelta(minutes=100)
    for item in candidates.find():
        individual_result = { "Candidate ID:":item["c_id"],
                              "Candidate Name":item["name"],
                              "votes": votes.find({"c_id":item["c_id"]}).count()
                              }
        candidates_result.append(individual_result)
        last_10m_votes  = votes.find({"vote_time":{"$gte":last_10m}}).count()
    output = {"Candidates_result":candidates_result,"Total_votes_last10m":last_10m_votes}
    return jsonify({'result':output})
```
    2. POST - @app.route('/vote/') - Vote individual candidate
```console
@app.route('/vote/<string:c_id>',methods=['POST'])
def vote_candidate(c_id):
    candidates = mongo.db.candidates
    votes = mongo.db.votes
    #Verify the candidate id
    c = candidates.find_one({"c_id":c_id})
    if c:
        vote =  {"c_id":c_id, "vote_time":datetime.datetime.now()}
        vote_id = votes.insert(vote)
        new_vote = votes.find_one({'_id':vote_id})
        output = {'name':new_vote['c_id'],'vote_time':new_vote['vote_time']}
    else:
        output ="No such candidates"
    return jsonify({'result':output})
```
## 5. Run the application

* Run app.py
```console
$ python app.py
```
## 6. Testing

* POST Request - Vote individual candidate

![GitHub Logo](https://github.com/sincheng/DEV-Offsite-Test/blob/master/Q3a/img/request_1.png)

* GET Request - Display result
![GitHub Logo](https://github.com/sincheng/DEV-Offsite-Test/blob/master/Q3a/img/request_2.png)

* Error Handling
    * Invalid candidate ID
```console
{
    "result": "No such candidates"
}
```
