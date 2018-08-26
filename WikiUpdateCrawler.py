import requests
import re

url = "https://en.wikipedia.org/wiki/"

print("Enter Page Name")
page = input()
page = "_".join(page.title().split())
url += page

try:
    data = requests.get(url).text
    info = re.search("last edited on ", data).start()
    print(data[info : info + 50].split('<')[0])

except:
    print("Page not found")