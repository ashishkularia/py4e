import urllib.request, urllib.parse, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certification notification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all span tags
tags = soup('span')
sum = 0
for tag in tags:
    sum = sum + float(tag.contents[0])
print(sum)