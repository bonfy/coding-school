# coding: utf-8

from flask import Flask, request, make_response

app = Flask(__name__)


# export FLASK_APP=app.py
# flask run

def get_cross_response(text, method='GET'):
    rst = make_response(text)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    rst.headers['Access-Control-Allow-Methods'] = method
    return rst


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    print(request.method)
    if request.method == 'GET':
        args = request.args
        name = args.get('name', 'NameNotSet')
        result = f'Hello GET {name}'
        return get_cross_response(result)
    if request.method == 'POST':
        # Content-Type: x-www-form-urlencoded
        args = request.form
        name = args.get('name', 'NameNotSet')
        result = f'Hello POST {name}'
        return get_cross_response(result, method='POST')
    result = 'Method not found!'
    return get_cross_response(result)
