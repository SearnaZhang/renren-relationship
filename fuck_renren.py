import urllib2
import urllib
import cookielib
import re
from lxml import etree

data={"email":"searna@sina.com.cn","password":"Searna1991"}
post_data=urllib.urlencode(data )
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
req=urllib2.Request("http://www.renren.com/PLogin.do",post_data)
content=opener.open(req)
#print content.read().decode('utf-8')
# uid_pattern = re.compile('renren\.com/(\d+)/profile')
req2 = urllib2.Request("http://www.renren.com/profile.do")
content = opener.open(req2)
uid_pattern = re.compile('renren\.com/(\d+)/profile')
uid = uid_pattern.findall(content.geturl())
print "http://friend.renren.com/GetFriendList.do?curpage={0}&id=" + uid[0]
FriendListRequest = urllib2.Request("http://friend.renren.com/GetFriendList.do?curpage={0}&id=" + uid[0])
content = opener.open(FriendListRequest)
 # print content.geturl()
uid_pattern = re.compile('id=(\d+)')
friends_uid = uid_pattern.findall(content.read())
tmp = ''
sumNum = 0
for ids in friends_uid:
	if tmp != ids:
		sumNum+=1
		print ids
	tmp = ids
print "sumNum=" + str(sumNum)
# parse = etree.HTMLParser()
# print etree.parse(content, parse)


# print uid