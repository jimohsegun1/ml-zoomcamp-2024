import requests

url='http://localhost:9797/predict'

patient = {
    "age"      :  37.0,
    "sex"      :   1.0,
    "cp"       :   2.0,
    "trtbps"   : 130.0,
    "chol"     : 250.0,
    "fbs"      :   0.0,
    "restecg"  :   1.0,
    "thalachh" : 187.0,
    "exng"     :   0.0,
    "oldpeak"  :   3.5,
    "slp"      :   0.0,
    "caa"      :   0.0,
    "thall"    :   2.0,
}

response = requests.post(url, json=patient).json()
print("Prediction for patient (0 = less chance of heart attack; 1 = more chance of heart attack):")
print(patient,"\n")
print(response)