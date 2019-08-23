from flask import Flask, Response, jsonify,request, abort
import json
import unittest
from utils.decorators import login_not_required, require_login
from apis.users_api import users_api
from apis.algorithms_api import algorithms_api
import configparser
import os
parser = configparser.SafeConfigParser(os.environ)
parser.read('config.ini')

app = Flask(__name__)
app.register_blueprint(users_api)
app.register_blueprint(algorithms_api)

#@app.before_request
def require_login_f():
    return require_login()

@app.route('/')
@login_not_required
def index():
    return parser['test']['test_1']
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3000')