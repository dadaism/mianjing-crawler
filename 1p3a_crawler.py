# -*- coding:utf-8 -*-
import urllib
import urllib2
import re 
import datetime
from datetime import timedelta

urls = [ 'http://www.1point3acres.com/bbs/forum-145-3.html',
         'http://www.1point3acres.com/bbs/forum-145-2.html',
         'http://www.1point3acres.com/bbs/forum-145-1.html'
       ]


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
lastDayDateTime = datetime.datetime.now() - timedelta(days = 1)
yesterday = lastDayDateTime.strftime('%Y-%-m-%-d')

def process_single_post(url):
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request).read()
    content = response.decode('GBK','ignore').encode('UTF-8')
    #unicode(response,'GBK').encode('UTF-8')

    ''' extract title '''
    p = re.compile(r'<span id="thread_subject">(.*?)</span>')
    titles = re.search(p, content)
    if titles is None:
        print url
        print
        return
    title = titles.group(1)
    print title
    
    ''' extract content '''
    p = re.compile(r'<td class="t_f".*?>(.*?)</td>', flags=re.DOTALL)
    items = re.search(p, content)
    if items is None:
        print "#### Lack of permission ####"
        return
    item = items.group(1)
    #print item
    #p = re.compile()
    item = re.sub(r'<font class="jammer">.*?/font>', '', item) # strip jammer
    item = re.sub(r'<div>.*?<h3><strong>.*?</span>.*?</div>', '', item, flags=re.DOTALL)# strip wanning
    item = re.sub(r'<[^>]*>', '', item)  # strip html tag
    item = re.sub(r'&amp;', '', item) # strip nothing
    item = re.sub(r'&nbsp;', '', item) # strip whitespace
    item = re.sub(r'&gt;', '>', item) # convert >
    item = re.sub(r'&lt;', '<', item) # convert <
    item = re.sub(r'&quot;', '"', item) # convert "
    #print item
    print    
    print '原帖地址：<a href="'+url+'" target="_blank">一亩三分地</a>'
    print '\n'.join( item.split('\n') )
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
            link = re.sub(r'amp;', '', link)
            #print link

            ''' extract title '''
            p = re.compile(r'<a.*?class="s xst">(.*?)</a>', flags=re.DOTALL)
            titles = re.search(p, item)
            title = titles.group(1)
            #print title

            ''' extract date '''
            p = re.compile('<em>.*?<span>.*?<span title="(.*?)">.*?</span>', flags=re.DOTALL)
            dates = re.search(p, item)
            date = ""
            #print dates
            if dates is not None:
                date = dates.group(1)
            else:
                continue
            #print date
            #print yesterday
            if yesterday == date:
                #print title
                #print link
                #print date
                #print
                process_single_post(link)
            
        #print content
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
