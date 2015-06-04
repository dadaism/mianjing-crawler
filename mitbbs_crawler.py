import urllib
import urllib2
 
 
page = 1
#url = 'http://www.qiushibaike.com/hot/page/' + str(page)
url = 'http://www.mitbbs.com/bbsdoc/JobHunting.html'
url = 'http://www.mitbbs.com/bbsdoc1/JobHunting_201_0.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request).read()
    response = unicode(response,'GBK').encode('UTF-8')
    print response
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason