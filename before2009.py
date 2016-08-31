#!/usr/bin/python
#coding=utf-8

import datetime
import sys
import tools

def getFixDict():

    fixDict = {
            #2008, according: http://www.gov.cn/gongbao/content/2008/content_859870.htm
            #2007, according: http://www.gov.cn/gongbao/content/2007/content_503397.htm
            #2006, according: http://www.gov.cn/jrzg/2005-12/22/content_133837.htm
            "2008":{
                "holiday":[
                    "0101", 
                    "0206", "0207", "0208","0209", "0210", "0211", "0212",
                    "0404", "0405", "0406",
                    "0501", "0502", "0503",
                    "0607", "0608", "0609",
                    "0913", "0914", "0915",
                    "0929", "0930", "1001", "1002", "1003", "1004", "1005"
                    ],
                "workDay":[
                    "0202", "0203",
                    "0504",
                    "0927", "0928",
                    ]
                },
            "2007":{
                "holiday":[
                    "0101", "0102", "0103",
                    "0218", "0219", "0220", "0221", "0222", "0223", "0224",
                    "0501", "0502", "0503", "0504", "0505", "0506", "0507",
                    "1001", "1002", "1003", "1004", "1005", "1006", "1007" 
                    ],
                "workDay":[
                    "0217", "0225",
                    "0428", "0429",
                    "0929", "0930",
                    "1229"
                    ]
                },
            "2006":{
                "holiday":[
                    "0101", "0102", "0103",
                    "0129", "0130", "0131", "0201", "0202", "0203", "0204",
                    "0501", "0502", "0503", "0504", "0505", "0506", "0507",
                    "1001", "1002", "1003", "1004", "1005", "1006", "1007" 
                    ],
                "workDay":[
                    "0128", "0205",
                    "0429", "0430",
                    "0930", "1008",
                    "1230", "1231"
                    ]
                }
            }

    return fixDict

def generate(year):
    fixDict = getFixDict()
    return generateAYear(year, fixDict[year])



def generateAYear(year, dic):
    holidaySet = set(dic["holiday"])
    workDaySet = set(dic["workDay"])

    beginDateTime = tools.strToDate(year + "0101")
    endDateTime = tools.strToDate(year + "1231")

    returnDict = {}

    with open(tools.FILE_DIR + year + ".txt", "w") as f:
        while beginDateTime <= endDateTime:
            dayStr = beginDateTime.strftime(tools.DATE_FORMAT)
            dayOfWeek = beginDateTime.weekday()
            beginDateTime +=  datetime.timedelta(days = 1)
            monthAndDay = dayStr[4:]

            result = tools.WORKDAY_MARK
            if dayOfWeek > 4:
                result = tools.RESTDAY_MARK

            if monthAndDay in workDaySet and monthAndDay in holidaySet:
                print "ERROR in day dict:" + year
                exit(1)
            if monthAndDay in workDaySet:
                result = tools.WORKDAY_MARK
            if monthAndDay in holidaySet:
                result = tools.HOLIDAY_MARK

            returnDict[dayStr] = result
            # skip work day since work day is mucher than rest day and holiday
            # And when we jude, we can't find a day in the cache, it's work day
            if result == tools.WORKDAY_MARK:
                continue
            f.write("%s\t%d\n" % (dayStr, result))

    return returnDict


def main():
    fixDict = getFixDict()
    for year, dic in fixDict.items():
        generateAYear(year, dic)


if __name__ == "__main__":
    main()


