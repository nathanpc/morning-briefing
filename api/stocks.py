#!/usr/bin/python

import requests

class Stocks:
    def __init__(self):
        return

    def get(self, ticker):
        """ Retrieves a stock/exchange rate value. """
        url = self._build_url(ticker)
        request = requests.get(url)
        csv = request.text.replace("\r\n", "").replace("\"", "").split(",")

        stock = { "name":   csv[0],
                  "ticker": csv[1],
                  "value":  csv[2],
                  "change": { "value": csv[3],
                              "percentage": csv[4] } }

        stock["value"] = float(stock["value"])
        stock["change"]["value"] = float(stock["change"]["value"])
        stock["change"]["percentage"] = float(stock["change"]["percentage"].replace("%", ""))

        return stock

    def _build_url(self, ticker):
        url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=nsl1c1p2&e=.csv"

        return url
