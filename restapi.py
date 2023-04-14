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

@app.route("/")
def hello_world():
    return "hello world"


@app.route("/add-data",methods=["get"])
def get_task():
    return flask.jsonify({"data": information})
