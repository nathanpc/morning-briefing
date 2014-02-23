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
                  "change_value": csv[3],
                  "change_perc": csv[4] }

        stock["value"] = float(stock["value"])
        stock["change_value"] = float(stock["change_value"])
        stock["change_perc"] = float(stock["change_perc"].replace("%", ""))

        return stock

    def _build_url(self, ticker):
        url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=nsl1c1p2&e=.csv"

        return url
