import flask

app = flask.Flask(__name__)

information = [
    {
        "Name" : "abhiraj",
        "age" : 23,
        "company" : "cloudeq",
        "Designation" : "Trainee"
    },

    {

        "Name" : "Akash",
        "age" : 23,
        "company" : "cloud ew",
        "Designation" : "SE"
    
    }
]

@app.route("/add-data",methods=["get"])
def get_task():
    return flask.jsonify({"data": information})


@app.route("/add-data",methods =["post"])
def get_task():
    if not flask.request.json :
        return flask.jsonify({'status': 'error'})
    newInfo = {'Name' :flask.request.json["Name"],'age': flask.request.json["age"]}
    information.append(newInfo)
  
return flask.jsonify({'status': 'success'})
app.run()

