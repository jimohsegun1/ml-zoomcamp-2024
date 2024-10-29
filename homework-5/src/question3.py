import pickle

MODEL_FILE = "model1.bin"
DV_DILE = "dv.bin"

CLIENT = {
    "job": "management",
    "duration": 400,
    "poutcome": "success",
}


def load_dv_and_model():
    with open(MODEL_FILE, "rb") as f_in:
        model = pickle.load(f_in)
    with open(DV_DILE, "rb") as f_in:
        dv = pickle.load(f_in)

    return (dv, model)


def predict(dv, model, client):
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    return y_pred


def main():
    dv, model = load_dv_and_model()
    y_pred = predict(dv, model, CLIENT)
    print(round(y_pred, 3))


if __name__ == "__main__":
    main()
