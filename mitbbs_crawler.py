# -*- coding:utf-8 -*-
import urllib
import urllib2
import re 
 
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
    pattern = re.compile('<a class="news1".*?>\n.*?/a>')
    #pattern = re.compile('.*面.*')
    items = re.findall(pattern,content)

    for item in items:
    	print item
    #print content
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason