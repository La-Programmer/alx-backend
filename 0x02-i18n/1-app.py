#!/usr/bin/env python3
"""Flask application Module"""

from flask import Flask, render_template, Request
from flask_babel import Babel


class Config:
    """Config Class for flask"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def hello():
    """Root route for flask app"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """Main Function"""
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)
