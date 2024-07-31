#!/usr/bin/env python3
"""Flask application"""

from flask import Flask, render_template, request, g, flash
from flask_babel import Babel, gettext, _
from pytz import timezone, exceptions


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
    params = request.args
    headers = request.headers
    if 'locale' in params and params['locale'] in Config.LANGUAGES:
        return params["locale"]
    elif g.user is not None and g.user['locale'] in Config.LANGUAGES:
        return g.user['locale']
    elif 'locale' in headers and headers['locale'] in Config.LANGUAGES:
        return headers['locale']
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


def get_timezone() -> str:
    """Get user's timezone info"""
    params = request.args
    headers = request.headers
    if 'timezone' in params and params['timezone'] in Config.LANGUAGES:
        try:
            zone = timezone(params['timezone'])
        except exceptions.UnknownTimeZoneError:
            zone = 'UTC'
        finally:
            return zone
    elif g.user is not None and g.user['timezone'] in Config.LANGUAGES:
        try:
            zone = timezone(g.user['timezone'])
        except exceptions.UnknownTimeZoneError:
            zone = 'UTC'
        finally:
            return zone
    else:
        return Config.BABEL_DEFAULT_TIMEZONE


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def hello() -> str:
    """Root route"""
    if g.user is not None:
        username = g.user['name']
    else:
        username = None
    return render_template('7-index.html', username=username)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.before_request
def before_request():
    """Execute before all requests"""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None

def get_user():
    """Get user function"""
    args = request.args
    login_as = int(args['login_as']) if 'login_as' in args else None
    if 'login_as' not in args or login_as not in users.keys():
        return None
    else:
        return users[login_as]


if __name__ == '__main__':
    """Main Function"""
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)
