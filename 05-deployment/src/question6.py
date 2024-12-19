import requests


def main():
    url = "http://localhost:5000/predict"
    client = {"job": "management", "duration": 400, "poutcome": "success"}
    response = requests.post(url, json=client).json()
    print(round(response["probability"], 3))


if __name__ == "__main__":
    main()