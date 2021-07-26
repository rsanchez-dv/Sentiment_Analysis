from flask import Flask, request, render_template
import os
import pickle
#from keras.models import load_model
#import tensorflow as tf

#from keras.preprocessing.text import Tokenizer
#from keras.preprocessing.sequence import pad_sequences

loaded_model_linReg = pickle.load(open("linReg_model.sav", "rb"))

#os.environ["CUDA_VISIBLE_DEVICES"] = '-1'
#os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

app = Flask(__name__)

'''
loaded_model = load_model('review_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer_json = pickle.load(handle)
tk = tf.keras.preprocessing.text.tokenizer_from_json(
    tokenizer_json
)
'''


@app.route('/', methods=["GET", "POST"])
def home():
    message = "Welcome to my flask based web application ... !!!"
    return render_template("home.html", message=message)


@app.route('/getPrediction', methods=["GET", "POST"])
def getPrediction():
    incoming_text = request.form["review_text"]
    print(incoming_text)
    #res = make_prediction_keras(incoming_text)
    res = make_prediction_linReg(incoming_text)
    print(res)
    return res


''' 
def make_prediction_keras(text):
    incoming_text = [text]
    print(incoming_text)
    print(type(incoming_text))
    # tk.fit_on_texts(incoming_text)
    print("OH NO")
    padded_text = pad_sequences(
        tk.texts_to_sequences(incoming_text), maxlen=100)
    print(padded_text)
    res = loaded_model.predict(padded_text)
    # loaded_model.clear_session()
    #res = [[0, .3], [0, .4]]
    print(res)
    for x in res:
        if x[1] > .5:
            return "Positive"
        else:
            return "Negative"
'''


def make_prediction_linReg(text):
    res = loaded_model_linReg.predict([text])
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
    app.run(debug=True)
