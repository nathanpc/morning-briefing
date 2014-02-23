#!/usr/bin/python

# TODO: Implement the weather update.
# TODO: Implement the stock+exchange update.
# TODO: Implement the RSS thing.

import json

from stocks import *
from weather import *

final_hash = { "stocks": None,
               "weather": None }

stocks = Stocks()
final_hash["stocks"] = stocks.get("GOOG")

weather = Weather()
final_hash["weather"] = weather.get("Vitoria, Espirito Santo")

print json.dumps(final_hash, indent = 4)
