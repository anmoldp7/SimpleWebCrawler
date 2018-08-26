import urllib.request
import re

print("Enter page name")

url = "https://en.wikipedia.org/wiki/"
name = input()
name = "_".join(name.title().split())
url += name

try:
    data = urllib.request.urlopen(url).read().decode("utf-8")
    m = re.search("last edited on ", data).start()
    print(data[m : m + 50].split('<')[0])

except:
    print("Page not found")