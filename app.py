from flask import Flask
import main as ml
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():

    return "Hello World!"

@app.route('/book/<string:text>/', methods=['GET','POST'])
def extract(text):
    keywords=ml.extract(text)
    result=ml.query(keywords)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105,debug=True)