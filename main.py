#!/usr/bin/python

import json
import flask

import api.api as API

app = flask.Flask(__name__, static_url_path = "")

@app.route("/api")
def api_request():
    api = API.API()
    final_hash = { "stocks": None,
                   "weather": None }

    final_hash["stocks"] = api.get_stock("GOOG")
    final_hash["weather"] = api.get_weather("Vitoria, Espirito Santo")

    return flask.Response(json.dumps(final_hash),
                          content_type = "application/json; charset=utf-8")

@app.route("/")
def index():
    return flask.render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
