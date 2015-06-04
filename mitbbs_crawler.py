# -*- coding:utf-8 -*-
import urllib
import urllib2
import re 
import datetime
from datetime import timedelta

page = 1
#url = 'http://www.qiushibaike.com/hot/page/' + str(page)
#url = 'http://www.mitbbs.com/bbsdoc/JobHunting.html'
url = 'http://www.mitbbs.com/bbsdoc1/JobHunting_1_0.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request).read()
    content = unicode(response,'GBK').encode('UTF-8')
    #pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
    #                 '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    #pattern = re.compile(r'<a class="news1".*?>.*?/a>', flags=re.DOTALL)
    #pattern = re.compile('.*面.*')
    ''' extract each title ''' 
    pattern = re.compile(r'<tr>.*?<td class="black4".*?</tr>', flags=re.DOTALL)
    items = re.findall(pattern,content)

    for item in items:
    	#print item
        ''' extract url '''
        p = re.compile(r'href="(/article_t.*?)"')
        urls = re.search(p,item)
        url = "http://www.mitbbs.com"+urls.group(1)
        #print url
        
        ''' extract title '''
        p = re.compile('<a class="news1".*?>.*?\n\s+(.*?)\s+</a>', flags=re.DOTALL)
        titles = re.search(p, item)
        title = titles.group(1)
        #print title
        
        ''' extract date '''
        p = re.compile(r'<span class="black10">(.*?)</span>')
        date = re.search(p, item).group(1)
        #print date

        mj_pattern = re.compile('(.*?面.*?\s)|(.*?on\s?site.*?\s)')
        tmp = re.findall(mj_pattern,title)

        lastDayDateTime = datetime.datetime.now() - timedelta(days = 1)
        yesterday = lastDayDateTime.strftime('%Y-%m-%d')
        if yesterday == date and tmp:
            print title, date
        #if tmp:
        #    print tmp[0]
    #print content
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason