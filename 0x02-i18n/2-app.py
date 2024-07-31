#!/usr/bin/env python3
"""Flask application"""

from flask import Flask, render_template, Request
from flask_babel import Babel


class Config:
    """Config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale() -> str:
    """Get locale"""
    return Request.accept_languages.best_match(Config.LANGUAGES)


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)
app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route("/")
def hello() -> str:
    """Root route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """Main Function"""
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)
