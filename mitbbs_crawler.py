# -*- coding:utf-8 -*-
import sys
import urllib
import urllib2
import re 
import datetime
from datetime import timedelta

reload(sys)
sys.setdefaultencoding("utf-8")

urls = [ 
         'http://www.mitbbs.com/bbsdoc1/JobHunting_401_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_301_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_201_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_101_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_1_0.html'
       ]


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

def process_single_post(url):
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request).read()
    content = unicode(response,'GBK', errors='ignore').encode('UTF-8')

    ''' extract title '''
    p = re.compile(r'<strong>同主题阅读：(.*?)</strong>')
    titles = re.search(p, content)
    title = titles.group(1)
    print title
    
    ''' extract content '''
    p = re.compile(r'<td\s+class="jiawenzhang-type">(.*?)--.*?</td>', flags=re.DOTALL)
    items = re.search(p, content)
    item = items.group(1)
    item = re.sub(r'<[^>]*>', '', item)  # strip html tag
    item = re.sub(r'&nbsp;', '', item)

    print    
    print '原帖地址：<a href="'+url+'" target="_blank">mitbbs</a>'
    print 
    print '\n'.join( item.split('\n')[5:] )
    print
    #print item
    #print content
    return

for url in urls:
    try:
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request).read()
        content = unicode(response,'GBK').encode('UTF-8')
    
        ''' extract each title ''' 
        pattern = re.compile(r'<tr>.*?<td class="black4".*?</tr>', flags=re.DOTALL)
        items = re.findall(pattern,content)

        for item in items:
        	#print item
            ''' extract link '''
            p = re.compile(r'href="(/article_t.*?)"')
            links = re.search(p,item)
            link = "http://www.mitbbs.com"+links.group(1)
            #print link
        
            ''' extract title '''
            p = re.compile('<a class="news1".*?>.*?\n\s+(.*?)\s+</a>', flags=re.DOTALL)
            titles = re.search(p, item)
            title = titles.group(1)
            #print title
        
            ''' extract date '''
            p = re.compile(r'<span class="black10">(.*?)</span>')
            date = re.search(p, item).group(1)
            #print date

            #mj_pattern = re.compile('(.*?面.*?\s)|(.*?on\s?site.*?\s)|(interview)', re.IGNORECASE)
            mj_pattern = re.compile('(面)|(on\s?site)|(interview)', re.IGNORECASE)
            tmp = re.findall(mj_pattern,title)
            #if tmp:
            #    print title, date
            lastDayDateTime = datetime.datetime.now() - timedelta(days = 1)
            yesterday = lastDayDateTime.strftime('%Y-%m-%d')
            #print yesterday
            if yesterday == date and tmp:
                #print title, date
                process_single_post(link)
        
        #print content
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
