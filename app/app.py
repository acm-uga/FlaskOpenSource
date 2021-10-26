#This is starter code for a basic flask application
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'
