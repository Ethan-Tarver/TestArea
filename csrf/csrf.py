from flask import Flask, make_response
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf


app = Flask(__name__)
CSRFProtect(app)

class Config(object):
    SECRET_KEY = "SDFJLAKDJFWOERWEIOTWEGDFGDS"

app.config.from_object(Config)

@app.after_request
def after_request(response):
    csrf_token = generate_csrf()
    response.set_cookie("csrf_token", csrf_token)
    return response


@app.route('/')
def csrf():
    return "hello"


if __name__ == "__main__":
    app.run()