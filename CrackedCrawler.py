import requests
import bs4
import re
import urllib.parse

def parse_title(title):
    return ' '.join(urllib.parse.unquote(title, encoding="utf-8", errors="replace").split('+'))

url = "http://www.cracked.com/"
soup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
x = soup.find_all('h3')
print('#' * 80)
for s in x:
    if s.find('a') is not None:
        p = s.find('a')
        print(parse_title(p["title"]))
print('#' * 80)