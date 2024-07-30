#!/usr/bin/env python3
"""Flask application"""

from flask import Flask, render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
babel = Babel(app)
babel.default_locale = Config.LANGUAGES[0]
babel.default_timezone = 'UTC'

@app.route("/")
def hello():
    """Root route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """Main Function"""
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)
