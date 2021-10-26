# This is starter code for a basic flask application
from flask import Flask
# this method is used to render html pages for ur app
from flask import render_template
# this is handling request data (GET,POST,PUT,etc.)
from flask import request

app = Flask(__name__)

# this endpoint is our home endpoint and returns hello world
@app.route('/')
def hello():
    return 'Hello World'

# this end point will render your html template from your !!! templates folders
@app.route('/htmlTemplate')
def htmlTemplate():
    return render_template('htmlPage.html')

# this end point renders inline html
@app.route('/htmlInline')
def htmlInline():
    return """
    <body>
    <h1> This is inline html ... it is not recommended because it is messy </h1>
    <p> AND I HATE MESSY >:( SO DON'T THINK ABOUT IT </p>
    </body>
    """

# this endpoint lets you read part of the url as a parameter
@app.route('/yourName/<name>')
def yourName(name):
    return ("This is the page for " + name)

# this is just a basic get request and is usually the default 
@app.route('/requests/get')
def getRequest():
    return "Most websites you visit are GET requests"

# This endpoint allows you to pass in parameters from your get request
# http://localhost:5000/requests/getWithParam?username=brandon&password=password
@app.route('/requests/getWithParam', methods=['GET'])
def getRequestWithParam():
    string = ""
    for x in request.args.to_dict():
        string = string + "Parameter Name:\t " + x + "\tParameter value:\t " + request.args.to_dict()[x] + "<br>"
    return "The parameters you passed are <br> " + string

# This endpoint is a post request and is used to pass in hidden data
@app.route('/requests/post', methods=['POST'])
def postRequest():
    return ""


###########################################################################################
# add your own endpoint here ... you can get creative with it and ask me for ideas!
