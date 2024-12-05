import pickle
from flask import Flask, request, jsonify

model_file = 'Model/heart-model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('heart')

@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()

    X = dv.transform([patient])
    y_pred = model.predict_proba(X)[:,1]
    score = int(y_pred[0] >= 0.50)
    return jsonify(score)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=9797)