#!/usr/bin/python
#coding=utf-8

import datetime
import json
import os
import re
import sys
import tools


def crawlBaidu(url):
    page = tools.getPage(url)
    page = re.sub("<.*?>\0*", "", page)
    dayDict = json.loads(page)
    return dayDict


def mergeHoliday(dayList):
    # fix the bug of baidu api: 
    #     bug:  A holiday's near day is rest day, 
    #           example {"20160101":2, "20160102":1, "20160103":1}
    #     but what I need is {"20160101":2, "20160102":2, "20160103":2}
    #
    dayList = [[item[0], int(item[1])] for item in dayList]
    dayList = sorted(dayList, key=lambda v:v[0])

    i = 0
    while i < len(dayList):
        if dayList[i][1] == tools.WORKDAY_MARK:
            i += 1
            continue

        mark = tools.RESTDAY_MARK
        j = i
        while j < len(dayList):
            if dayList[j][1] == tools.HOLIDAY_MARK:
                mark = tools.HOLIDAY_MARK
            if dayList[j][1] == tools.WORKDAY_MARK:
                break
            j += 1

        for k in range(i, j):
            dayList[k][1] = mark

        i = j

    return dict(dayList)



def crawlAYear(year):
    if os.path.exists(tools.FILE_DIR + year + ".txt"):
        return

    # if crawl togather, the baidu api may return error (I noticed it after tested)
    # so cut it to two part
    dayDictFirst = crawlInterval(year + "0101", year + "0630")
    dayDictSecond = crawlInterval(year + "0701", year + "1231")
    returnDict = dict(dayDictFirst.items() + dayDictSecond.items())
    returnDict = mergeHoliday(returnDict.items())

    # result == 1 -> rest day
    # result == 2 -> holiday
    with open(tools.FILE_DIR + year + ".txt", "w") as f:
        for result in sorted(returnDict.items(), key=lambda v:v[0]):
            # skip work day since work day is mucher than rest day and holiday
            # And when we jude, we can't find a day in the cache, it's work day
            if result[1] == tools.WORKDAY_MARK:
                continue
            f.write("%s\t%d\n" % result)

    return returnDict


def crawlInterval(beginDayStr, endDayStr):

    if not (tools.isValidDateStr(beginDayStr) and tools.isValidDateStr(endDayStr)):
        print "ERROR: begin day or end day's format error"
        exit(1)

    if beginDayStr > endDayStr:
        print "ERROR: Begin day is later than end day"
        exit(1)

    daySetList = [set(), set()]
    pattern =  "http://apis.baidu.com/xiaogg/holiday/holiday?d=%s"


    beginDateTime = tools.strToDate(beginDayStr)
    endDateTime = tools.strToDate(endDayStr)

    dayPara = ""
    while beginDateTime <= endDateTime:
        dayStr = beginDateTime.strftime(tools.DATE_FORMAT)
        beginDateTime +=  datetime.timedelta(days = 1)
        dayPara += dayStr + ","

    dayPara = dayPara[:-1]
    return crawlBaidu(pattern % dayPara)

if __name__ == "__main__":
    crawlAYear(*sys.argv[1:])


