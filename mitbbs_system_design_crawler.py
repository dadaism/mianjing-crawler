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

reload(sys)
sys.setdefaultencoding("utf-8")

urls = [ 'http://www.mitbbs.com/bbsdoc1/JobHunting_301_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_201_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_101_0.html',
         'http://www.mitbbs.com/bbsdoc1/JobHunting_1_0.html'
       ]


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
    
def sd_process_single_post(url):
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request).read()
    content = unicode(response,'GBK', errors='ignore').encode('UTF-8')
    
    soup = BeautifulSoup(content, 'html.parser')

    ''' extract date '''
    #p = re.compile(r'[0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{4}', flags=re.DOTALL)
    p = re.compile(r'[0-9]{4}年[0-9]{2}月[0-9]{2}日', flags=re.DOTALL)
    dates = re.findall(p,content)
    if not dates:
        date = "xxxx-xx-xx"
    else:
        date = dates[0]

    ''' extract title '''
    p = re.compile(r'<strong>同主题阅读：(.*?)</strong>')
    titles = re.search(p, content)
    title = titles.group(1)
    #print title
    
    ''' extract content '''
    #first_content = soup.find('td', { 'class':'jiawenzhang-type'})
    #print first_content

    p = re.compile(r'<td\s+class="jiawenzhang-type">(.*?)--.*?</td>', flags=re.DOTALL)
    items = re.search(p, content)
    item = items.group(1)
    item = re.sub(r'<[^>]*>', '', item)  # strip html tag
    item = re.sub(r'&nbsp;', '', item)
    first_text = '\n'.join( item.split('\n')[5:] ) # skip first 4 lines

    sd_pattern = re.compile('(system)|(design)|(系统)|(设计)''', re.IGNORECASE)
    if re.search(sd_pattern, title) or re.search(sd_pattern, first_text):
        print
        print date
        print 
        print title
        print 
        print '原帖地址：<a href="'+url+'" target="_blank">mitbbs</a>'
        print 
        print first_text
        print
    
    #print item
    #print content
    return

for url in urls:
    #sleep(randint(1,5))
    sleep(0.1)
    try:
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request).read()
        content = unicode(response,'GBK', errors='ignore').encode('UTF-8')
        #content = response;
    
        ''' extract each post ''' 
        soup = BeautifulSoup(content, 'html.parser')
        items = soup.select('strong a')
        
        for item in items:
            #print item
            title = item.get_text()
            link = "http://www.mitbbs.com"+item.get('href')
            #print link
            #sd_pattern = re.compile('(面)|(题)|(on\s?site)|(interview)|(system)|(design)|(系统)|(设计)', re.IGNORECASE)
            if re.search(sd_pattern, title):
                #print title
                #print link
                sd_process_single_post(link)
                break


    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
