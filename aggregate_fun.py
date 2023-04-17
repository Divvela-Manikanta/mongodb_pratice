from pymongo import MongoClient
from flask import Flask,request
app = Flask(__name__)
app2 = MongoClient("localhost",27017)
db = app2.project2
collection  = db.document


data = collection.aggregate([{
    "$match":{"gender":"m"}},
    {"$group":{"_id":"$gender","toatal":{"$sum":1}}}

    # {"$group":{"_id":"$gender","toatal_sum":{"$sum":1}}}

])

for x  in data:
    print(x)

@app.route("/agg",methods=["post"])
def agg():
    data = request.get_json()
    output = collection.aggregate(data)

    for val in output:
        print(val)
    return "done"
@app.route("/avg",methods=["post"])
def avg():
    data = request.get_json()
    output = collection.aggregate(data)

    for val in output:
        print(val)
    return "done"

@app.route("/sl/<int:data>")
def sl():
    output = collection.aggregate(
        {"$skip":2}
    )


if __name__ == "__main__":
    app.run(debug=True,port=6000)
output = collection.find({})
for val in output:
    print(val)
print("-----------------------------------")
output = collection.aggregate([{"$group":{"_id":"$full_name","count":{"$sum":1}}},{"$sort":{"count":-1}}])
for val in output:
    print(val)