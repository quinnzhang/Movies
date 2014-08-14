import re

for i in range (1000,2001):
	print "http://www.imdb.com/search/title?at=0&count=100&sort=moviemeter,asc&start=" + str(100*i + 1) + "&title_type=feature"