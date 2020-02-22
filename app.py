from flask import Flask,render_template,url_for,request
import pandas as pd
from polarity import zack_pol

################################
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST', 'GET'])  # /result route, allowed request methods; POST, and GET
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        df = pd.read_csv('lex_90000_mill_words_sample_filter.csv')
        lex2 = df.set_index("word")
        lex2 = lex2.to_dict()['polarityScore']
        my_prediction = zack_pol(data, lex2).score()
        my_prediction = round(my_prediction, 4)
        return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=8080)
