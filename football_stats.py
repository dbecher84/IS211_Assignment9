#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""get top 20 football players from cbs sports"""


import urllib2
from bs4 import BeautifulSoup


SITE_URL = urllib2.urlopen('https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns')
BEAUTIFUL_INFO = BeautifulSoup(SITE_URL, "lxml")
TABLE = BEAUTIFUL_INFO.find_all("table", attrs={"class":"data"})[0].find_all("tr",
                                                                             attrs={"valign":"top"})


def top_touchdowns():
    """list the top 20 players in touchdowns accroding to cbs sports"""
    print "The top 20 players with the most touchdowns are"
    count = 0
    for item in TABLE:
        if count <= 19:
            name = item.find_all('td')[0].find_all('a')[0].contents[0]
            pos = item.find_all('td')[1].contents[0]
            team = item.find_all('td')[2].find_all('a')[0].contents[0]
            tds = item.find_all('td')[6].contents[0]
            count += 1
            print ("Player: {}, {}, Team: {}, "
                   "Position: {}, TDs: {}").format(count, name, team, pos, tds)


if __name__ == "__main__":
    top_touchdowns()
