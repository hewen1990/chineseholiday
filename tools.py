#!/usr/bin/python
#coding=utf-8

import urllib2
import datetime

DATE_FORMAT = "%Y%m%d"
FILE_DIR = "./data/"
HOLIDAY_MARK = 2
RESTDAY_MARK = 1
WORKDAY_MARK = 0

def isValidDateStr(dateStr):
    try:
        datetime.datetime.strptime(dateStr, DATE_FORMAT)
        return True
    except:
        return False
    return None

def strToDate(dateStr):
    return datetime.datetime.strptime(dateStr, DATE_FORMAT)


def minusDate(dateStr1, dateStr2):
    delta = strToDate(dateStr1) - strToDate(dateStr2)
    return delta.days

def getPage(url):
    headers = [
            "apikey:494969c1cb7d9d1b05960c7257750648"
            ]

    req = urllib2.Request(url)
    for header in headers:
        header = header.split(":", 1)
        header = [h.strip() for h in header]
        req.add_header(header[0], header[1])

    page = urllib2.urlopen(req).read()
    return page



if __name__ == "__main__":
    pass


