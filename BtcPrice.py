#!/usr/bin/python
from sense_hat import SenseHat
import requests, json
from time import sleep


def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print "Error querying Bitstamp API"

while True:
        BtcPrice = "BTC: " + str(getBitcoinPrice())
        sense = SenseHat()
        red = (255, 0, 0)
        sense.show_message(BtcPrice, text_colour = red)
    
