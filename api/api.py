#!/usr/bin/python

# TODO: Implement the RSS thing.

import json

from stocks import *
from weather import *

class API:
    def __init__(self):
        return

    def get_stock(self, ticker):
        stocks = Stocks()
        return stocks.get(ticker)

    def get_weather(self, location, metric = True):
        weather = Weather()
        return weather.get(location, metric)

# Testing standalone.
if __name__ == "__main__":
    api = API()
    final_hash = { "stocks": None,
                   "weather": None }

    final_hash["stocks"] = api.get_stock("GOOG")
    final_hash["weather"] = api.get_weather("Vitoria, Espirito Santo")

    print json.dumps(final_hash, indent = 4)
