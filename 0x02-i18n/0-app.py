#!/usr/bin/env python3
"""Flask application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """Root route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """Main Function"""
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)
