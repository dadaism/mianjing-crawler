# -*- coding:utf-8 -*-
import sys
import urllib
import urllib2
import re 
import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
from random import randint
from time import sleep

urls = [ 'http://www.mitbbs.com/bbsdoc1/JobHunting_301_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_201_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_101_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_1_0.html'
       ]


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
    
def sd_process_single_post(url):

    return

for url in urls:
    try:
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request).read()
        content = unicode(response,'GBK').encode('UTF-8')

    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
