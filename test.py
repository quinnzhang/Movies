import re
import json

a = "1234 (a567,89)"

b = re.findall('\((.*?)\)',a)
c = re.findall('\d+', b[0])
d = ''.join(c)

print a
print b
print c
print d
