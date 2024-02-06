from flask import Flask, request

app = Flask(__name__)


@app.route("/",methods=['GET'])
def index():
    return {
        "message":"Hello world, this is assignment-2"
    }

@app.route("/add", methods=['GET'])
def add():

    a = request.args.get('a')
    b = request.args.get('b')

    if not (a or b):
        return {
            "error": "Need 2 numbers to add"
        }


    # convert to numbers

    a = float(a)
    b = float(b)

    return {
        "addition": a+b
    }
