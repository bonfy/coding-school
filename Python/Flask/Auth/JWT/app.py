# -*- coding:utf-8 -*-

from flask import Flask, jsonify, make_response, request
import jwt
import datetime
import functools


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesecretkey'


def token_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        # http://127.0.0.1:/route?token=xxxxxx
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def main():
    return '<h1>Hello World</h1>'


@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this'})


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'Only for user with token'})


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


if __name__ == '__main__':
    app.run(debug=True)
