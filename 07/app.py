# Initialize Project.
from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"
# def create_app(classfier):
    # app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
