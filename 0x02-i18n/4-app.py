#!/usr/bin/env python3
"""Flask application"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """Config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


def get_locale() -> str:
    """Get locale"""
    args = request.args
    if 'locale' not in args or args['locale'] not in Config.LANGUAGES:
        return request.accept_languages.best_match(Config.LANGUAGES)
    else:
        return args['locale']


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def hello() -> str:
    """Root route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    """Main Function"""
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)
