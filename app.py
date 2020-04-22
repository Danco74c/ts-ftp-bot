from exceptions import *
from conf import config
from flask import Flask, Response, request
from handlers import command_handler



app = Flask(__name__)


@app.route("/slack/commands", methods=["GET", "POST"])
def commands():

    responseStr = ""
    response_url = request.form.get("response_url")

    try:
        responseStr = command_handler(request.form.get('text',None),response_url)
    except FTPIncorrectSyntax as e:
        responseStr = e.message
    except FolderAlreadyExists as e:
        responseStr = e.message
  
    
    response = Response(responseStr, status=200, mimetype='application/json')
    return response

@app.route("/health", methods=["GET"])
def check_health():
    response = Response("I'm fine", status=200, mimetype='application/json')
    return response



app.run(host='0.0.0.0', debug=True, port=8080)

