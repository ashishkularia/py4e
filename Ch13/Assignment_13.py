import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL Certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter XML URL: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
fh = urllib.request.urlopen(url, context=ctx)
xxml = fh.read()
data = ET.fromstring(xxml)
lst = data.findall('comments/comment')
sum = 0
for x in lst:
    sum = sum + int(x.find('count').text)
print(sum)