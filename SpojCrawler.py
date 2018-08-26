import requests
import sys
import re
from bs4 import BeautifulSoup

def scraper(data):
    soup = BeautifulSoup(data, "html.parser")
    print("#" * 80)
    x = soup.find("img", {"class" : "avatar small-left-margin"})
    x = x.parent.find("h3")
    if x is not None:
        print("Profile Name: " + x.string)
    x = x.parent.find("h4")
    if x is not None:
        print("Handle      : " + x.string[1:])
    x = soup.find("i", { "class" : "fa fa-map-marker"})
    if x is not None:
        print("Location    : " + list(x.parent.children)[1][1 : ])
    x = soup.find_all("i", {"class" : "fa fa-trophy"})
    p = None
    for s in x:
        if s.parent.parent.find("p") is not None:
            p = s
    if p is not None:
        info = p.parent.text.split("#", 1)[1].split(' ', 1)
        print("World Rank  : " + info[0])
        print("Points      : " + info[1][1 : -8])
    x = soup.find("dl", {"class" : "dl-horizontal profile-info-data profile-info-data-stats"})
    if x is not None:
        print("Solved      : " + x.find_all("dd")[0].text)
        print("Submissions : " + x.find_all("dd")[1].text)
    print("#" * 80)

url = "https://www.spoj.com/users/"

print("Enter handle.")
handle = input()
url += handle

try:
    data = requests.get(url).text
    scraper(data)
except:
    print("Invalid Handle")