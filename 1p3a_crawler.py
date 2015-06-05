# -*- coding:utf-8 -*-
import urllib
import urllib2
import re 
import datetime
from datetime import timedelta

urls = [ #'http://www.1point3acres.com/bbs/forum-145-3.html',
         #'http://www.1point3acres.com/bbs/forum-145-2.html',
         'http://www.1point3acres.com/bbs/forum-145-1.html'
       ]


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

def process_single_post(url):
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request).read()
    content = unicode(response,'GBK').encode('UTF-8')

    ''' extract title '''
    #p = re.compile(r'<strong>同主题阅读：(.*?)</strong>')
    #titles = re.search(p, content)
    #title = titles.group(1)
    #print title
    
    ''' extract content '''
    #p = re.compile(r'<td\s+class="jiawenzhang-type">(.*?)--.*?</td>', flags=re.DOTALL)
    #items = re.search(p, content)
    #item = items.group(1)
    #item = re.sub(r'<[^>]*>', '', item)  # strip html tag
    #item = re.sub(r'&nbsp;', '', item)

    print    
    print '原帖地址：<a href="'+url+'" target="_blank">mitbbs</a>'
    print 
    #print '\n'.join( item.split('\n')[5:] )
    print
    #print item
    #print content
    return

for url in urls:
    try:
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request).read()
        content = unicode(response,'GBK').encode('UTF-8')
    
        ''' extract each item ''' 
        pattern = re.compile(r'<tbody id="normalthread_.*?>.*?</tbody>', flags=re.DOTALL)
        items = re.findall(pattern,content)

        for item in items:
        	#print item

            ''' extract link '''
            p = re.compile('<a href="(.*?)"')
            links = re.search(p, item)
            link = links.group(1)
            print link

            ''' extract title '''
            p = re.compile(r'<a.*?class="s xst">(.*?)</a>', flags=re.DOTALL)
            titles = re.search(p, item)
            title = titles.group(1)
            print title

            ''' extract date '''
            
        
            print 
        #print content
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
