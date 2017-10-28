#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""get the weather forcast"""


import urllib2
from bs4 import BeautifulSoup


SITE_URL = urllib2.urlopen('https://www.wunderground.com/history/airport/KNYC/2017/10/28/MonthlyCalendar.html?req_city=Central%20Park&req_state=NY&reqdb.zip=10106&reqdb.magic=2&reqdb.wmo=99999#calendar')
BEAUTIFUL_INFO = BeautifulSoup(SITE_URL, "lxml")
TABLE = BEAUTIFUL_INFO.find_all("table", attrs={"class":"dayTable"})


def past_temps():
    """finds the high temperature for the days that have passed in the month specified"""
    print "The past high temperature for the month are:"
    for item in TABLE:
        if item.find("a"):
            past_date = item.find("a").get_text().strip()

        if item.find("td", attrs={"class":"value-header"}, text=['Actual:']):
            past_high = item.find("span", attrs={"class":"high"}).find("span").get_text()[:2]
            print "On day {} of the month the high temperature was {} degrees.".format(past_date,
                                                                                       past_high)


def future_temps():
    """finds the high temperature for the days that have not passed in the month specified"""
    print "The highs for the rest of the month are:"
    for item in TABLE:
        if item.find("a"):
            date = item.find("a").get_text().strip()

        if item.find("td", attrs={"class":"value-header"}, text=['Forecast:']):
            high = item.find("span", attrs={"class":"high"}).get_text()[:2]
            print "On day {} of the month the forecasted temperature is {} degrees.".format(date,
                                                                                            high)


if __name__ == "__main__":
    past_temps()
    future_temps()
