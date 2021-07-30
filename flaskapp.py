from flask import Flask, request, render_template
import os
import pickle
import zipfile

with zipfile.ZipFile('svc_model.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

loaded_model = pickle.load(open("svc_model.sav", "rb"))

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    message = "Welcome to my flask based web application ... !!!"
    return render_template("home.html", message=message)


@app.route('/getPrediction', methods=["GET", "POST"])
def getPrediction():
    incoming_text = request.form["review_text"]
    print(incoming_text)
    res = make_prediction_linReg(incoming_text)
    print(res)
    return res


def make_prediction_linReg(text):
    res = loaded_model.predict([text])
    result = ""
    if res == 0:
        result = "Negative Review"
    elif res == 1:
        result = "Neutral Review"
    elif res == 2:
        result = "Positive Review"
    else:
        result = "UNKNOWN"
    return result


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
