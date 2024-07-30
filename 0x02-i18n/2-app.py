#!/usr/bin/env python3
"""Flask application"""

from flask import Flask, render_template, Request
from flask_babel import Babel

from config import Config


app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

@app.route("/")
def hello():
    """Root route"""
    return render_template('0-index.html')

@babel.localeselector
def get_locale():
    """Get locale"""
    return Request.accept_languages.best_match(Config.LANGUAGES)

if __name__ == '__main__':
    """Main Function"""
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)
