# Initialize Project.
from flask import Flask, request, jsonify
from PIL import Image


app = Flask(__name__)


def create_app(classifier):
    @app.route("/", methods=["POST"])
    def predict():
        # Get the received-file-handler.
        img_file = request.files["img"]

        # Check the file is empty
        if img_file.filename == "":
            return "Bad Request", 400

        # Read Image-File by using
        # PIL.
        img = Image.open(img_file)

        # Predict is Taco or Burrito
        # by using Classification-Model.
        result = classifier.predict(img)

        # Return Result as a 'JSON'-form.
        return jsonify({
            "result": result
        })
    return app


if __name__ == "__main__":
    app.run(debug=True)

