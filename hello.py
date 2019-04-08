from flask import Flask

app = Flask(__name__)

@app.route('/') # tell where to look
def hello():
    return 'Hello World!'

@app.route('/ds')
def ds():
    return 'Data Science is amazing'

