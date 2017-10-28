#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""get the past value of apple stock"""


import urllib2
from bs4 import BeautifulSoup


SITE_URL = urllib2.urlopen('https://finance.yahoo.com/quote/AAPL/history?ltr=1')

BEAUTIFUL_INFO = BeautifulSoup(SITE_URL, "lxml")

TABLE = BEAUTIFUL_INFO.find_all("table", attrs={"data-test":"historical-prices"})[0].find_all("tr", attrs={"class":"BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)"})


def apple_stock():
    """find recent apple stock value"""
    print "A sampling of past Apple stock values"
    for item in TABLE:
        date = item.find_all("td")[0].find_all("span")[0].contents[0]
        try:
            val = item.find_all("td")[4].find_all("span")[0].contents[0]
            print ("Date: {}, Closing Value: ${}").format(date, val)
        except IndexError:
            pass


if __name__ == "__main__":
    apple_stock()
