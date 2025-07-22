from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
from werkzeug.utils import secure_filename
import os
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Get absolute path to model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "best.pt")
model = YOLO(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(image_path)

            # Run prediction
            results = model(image_path)
            result_image = results[0].plot()
            result_filename = f"pred_{filename}"
            result_path = os.path.join(app.config["UPLOAD_FOLDER"], result_filename)
            cv2.imwrite(result_path, result_image)

            return redirect(url_for("result", orig=filename, pred=result_filename))
    return render_template("index.html")

@app.route("/result")
def result():
    orig = request.args.get("orig")
    pred = request.args.get("pred")
    return render_template("result.html", original=orig, predicted=pred)

if __name__ == "__main__":
    app.run(debug=True)
