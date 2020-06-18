# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:00:43 2020

@author: DELL
"""
import twitterscraper
import random
HEADERS_LIST = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
]
twitterscraper.query.HEADER = {'User-Agent': random.choice(HEADERS_LIST), 'X-Requested-With': 'XMLHttpRequest'}

from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
begin_date=dt.date(2020,5,19)
end_date=dt.date(2020,5,20)
limit=100000  #word limit
lang='english'
tweets=query_tweets("#HappyBirthdayNTR",begindate=begin_date,enddate=end_date,limit=limit,lang=lang)
df=pd.DataFrame(t.__dict__ for t in tweets)