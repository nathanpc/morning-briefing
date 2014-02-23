#!/usr/bin/python

import requests
import json

class Weather:
    def __init__(self):
        return

    def get(self, location, metric = True):
        """ Retrieves the weather forecast. """
        url = self._build_url(location, metric)
        request = requests.get(url)
        weather = json.loads(request.text)

        info = { "coord": weather["coord"],
                 "weather": weather["weather"][0],
                 "wind": weather["wind"],
                 "main": weather["main"] }

        return info

    def _build_url(self, location, metric):
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&mode=json"

        if metric:
            url += "&units=metric"
        else:
            url += "&units=imperial"

        return url
