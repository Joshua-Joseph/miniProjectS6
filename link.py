
# import modules
import requests
import re

from bs4 import BeautifulSoup

# link to extract html data
def getdata(url):
	r = requests.get(url)
	return r.text

htmldata = getdata("https://www.google.com/search?q=beautifulsoup+findall+links&biw=1301&bih=639&ei=LdwmYqTmO4iTseMPkcSb8AE&oq=findall+beautifulsoup+link+&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgQIABAKSgQIQRgASgQIRhgAUKMJWIITYOwhaAFwAXgAgAHbAYgBvgeSAQUwLjUuMZgBAKABAcgBCMABAQ&sclient=gws-wiz")
soup = BeautifulSoup(htmldata, 'html.parser')

for data in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
	print((re.split(":(?=http)",data["href"].replace("/url?q=","")))[0])
	
