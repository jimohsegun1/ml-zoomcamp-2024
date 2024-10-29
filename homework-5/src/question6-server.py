import pickle
from flask import Flask, jsonify, request

MODEL_FILE = "model2.bin"
DV_DILE = "dv.bin"


def load_dv_and_model():
    with open(MODEL_FILE, "rb") as f_in:
        model = pickle.load(f_in)
    with open(DV_DILE, "rb") as f_in:
        dv = pickle.load(f_in)
    return (dv, model)


dv, model = load_dv_and_model()
app = Flask("ml-zoomcamp")


@app.route("/predict", methods=["POST"])
def predict():
    client = request.get_json()
    y_pred = predict(dv, model, client)
    result = {
        "probability": float(y_pred),
    }
    return jsonify(result)


def predict(dv, model, client):
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    return y_pred


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
