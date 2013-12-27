'''
Created on 2013-1-27
@author: isaced
'''
import urllib2
Url = "http://www.oschina.net/"
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
req = urllib2.Request(url = Url,  headers = Headers)

html = urllib2.urlopen(req).read()
