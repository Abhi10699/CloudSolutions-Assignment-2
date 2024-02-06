from flask import Flask

app = Flask(__name__)


@app.route("/",methods=['GET'])
def index():
    return {
        "message":"Hello world, this is assignment-2"
    }


if __name__ == "__main__":
    app.run(
        port=8000,
        debug=True
    )
