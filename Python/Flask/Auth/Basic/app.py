# coding: utf-8

from flask import Flask, request, make_response
import functools

app = Flask(__name__)


def auth_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)

        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated


@app.route('/')
def main():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return '<h1>You Logged in</h1>'

    # return 'could not verify', 401
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route('/page')
@auth_required
def page():
    return '<h1>Main Page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
