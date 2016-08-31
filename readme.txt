

Chinese day's judge:


Judge a day is holiday or rest day or work day in Chinese:
    tool:  http://apistore.baidu.com/apiworks/servicedetail/1116.html

Cache the day data from http://apistore.baidu.com/apiworks/servicedetail/1116.html

NOTICE:
    I define a rest day near a holiday is holiday,
    example {"20160101":2, "20160102":2, "20160103":2}

    some says 20160102 is a rest day but not a holiday, and it's not the same
with me.
    

And all the files are as follows:
    .
    |-- before2009.py -> generate day before 2009 and after 2006
    |-- crawlBaidu.py -> crawl the day data from baidu api and store in ./data
    |-- data -> the cache data directory
    |   |-- 2006.txt
    |   |-- 2015.txt
    |   `-- 2016.txt
    |-- judgeDay.py -> the judge main file
    |-- readme.txt -> this file
    |-- test.py -> example of how use it
    `-- tools.py -> tools for the project


As in example of test.py:
    return 0 of a day -> the day is work day
    return 1 of a day -> the day is rest day
    return 2 of a day -> the day is holiday


Weakness:
    unsuport the day before 2006!!!
    and rely on baidu api



Thanks for: http://blog.wpjam.com/m/wpjam_is_holiday/

Any questions: hewen1990#gmail.com
