import pickle

import numpy as np
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[
        data["mean_radius"],
        data["mean_perimeter"],
        data["mean_area"],
        data["mean_concave_points"],
        data["mean_concavity"],
        data["worst_radius"],
        data["worst_perimeter"],
        data["worst_area"],
        data["worst_concave_points"],
        data["worst_concavity"]
    ]])

    pred = model.predict(features)[0]
    result = "Malignant (Cancer)" if pred == 0 else "Benign (No Cancer)"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)




