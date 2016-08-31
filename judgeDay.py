#!/usr/bin/python
#coding=utf-8

import before2009
import crawlBaidu
import os
import re
import tools

DATE_DICT = {}

def judge(dayStr):
    global DATE_DICT

    if not tools.isValidDateStr(dayStr):
        return None

    year = dayStr[:4]


    if year < "2006":
        print "unsupport before 2006"
        exit(1)

    if year not in DATE_DICT:
        if year >= "2009":
            DATE_DICT[year] = crawlBaidu.crawlAYear(year)
        else:
            DATE_DICT[year] = before2009.generate(year)

    # if we can't find a day in the cache, it's work day
    return DATE_DICT[year].get(dayStr, tools.WORKDAY_MARK)

def readAYearDay(year):
    dayDict = {}
    with open(tools.FILE_DIR + year + ".txt") as f:
        while 1:
            line = f.readline()
            if not line:
                break
            line = line.strip().split()
            dayDict[line[0]] = int(line[1])
    return dayDict

def main():
    files = os.listdir(tools.FILE_DIR)
    for f in files:
        if os.path.isfile(tools.FILE_DIR + f) and re.match("^\d{4}.txt$", f):
            year = f[:4]
            DATE_DICT[year] = readAYearDay(year)

main()

if __name__ == "__main__":
    pass


