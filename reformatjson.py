import re
import json
from decimal import Decimal

imdbtest100 = open('votes.json') # original json file here
imdbtest1003 = open('imdbpopvotes.json', 'w') # the empty new file to read the new data to

imdb = json.load(imdbtest100)

def num_there(s):
    return any(i.isdigit() for i in s)

for i in range(100000):
	if imdb[i]["rating"] and num_there(imdb[i]["rating"][0]):
		a = imdb[i]["rating"][0]
		imdb[i]["rating"] = float(a)
	else:
		imdb[i]["rating"] = 0

for i in range(100000):
	if imdb[i]["votes"] and num_there(imdb[i]["votes"][0]):
		a = imdb[i]["votes"][0]
		b = re.findall('\((.*?)\)',a)
		c = re.findall('\d+', b[0])
		d = ''.join(c)
		imdb[i]["votes"] = int(d)
	else:
		imdb[i]["votes"] = 0

for i in range(100000):
	if imdb[i]["title"]:
		a = imdb[i]["title"][0]
		imdb[i]["title"] = a
	else:
		imdb[i]["title"] = ''

for i in range(100000):
	if imdb[i]["length"]:
		a = imdb[i]["length"][0]
		b = re.findall('\d+', a)
		c = b[0]
		imdb[i]["length"] = int(c)
	else:
		imdb[i]["length"] = 0

for i in range(100000):
	if imdb[i]["year"]:
		a = imdb[i]["year"][0]
		b = re.findall('\d+', a)
		if b:
			c = b[0]
		else: 
			c = 0
		imdb[i]["year"] = int(c)
	else:
		imdb[i]["year"] = 0

for i in range(100000):
	if imdb[i]["url"]:
		a = imdb[i]["url"][0]
		b = "imdb.com"
		imdb[i]["url"] = b + a
	else:
		imdb[i]["url"] = "imdb.com"

for i in range(100000):
	if imdb[i]["genre"]:
		a = ','.join(imdb[i]["genre"])
		a = a.replace(',', ', ')
		imdb[i]["genre"] = a
	else:
		imdb[i]["genre"] = ""

json.dump(imdb, imdbtest1003, indent=2)
imdbtest100.close()
imdbtest1003.close()