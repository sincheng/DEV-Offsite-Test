from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'voting_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/voting_db'
mongo = PyMongo(app)

#Endpoint to display the result
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

#Endpoint to vote individual candidate
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


if __name__ == '__main__':
    app.run(port=5000, debug=True)
