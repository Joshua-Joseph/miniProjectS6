# import module
import requests
import re

from bs4 import BeautifulSoup

# link for extract html data


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata(
    "https://www.google.com/search?q=russsia&oq=russsia+&aqs=chrome..69i57.2172j0j9&sourceid=chrome&ie=UTF-8")
soup = BeautifulSoup(htmldata, 'html.parser')

for data in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print((re.split(":(?=http)", data["href"].replace(
        "/url?q=", "")))[0].split("&")[0])
