import urllib.request, urllib.parse, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certification notification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
for i in range(count):
    if i == 0:
        html = urllib.request.urlopen(url)
    else:
        html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[position-1]
    url = tag.get('href', None)
    print(tag.contents[0])


