# import module
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# link for extracting html data
def getdata(url):
	r = requests.get(url)
	return r.text

htmldata = getdata("https://www.google.com/search?q=beautifulsoup+findall+links&biw=1301&bih=639&ei=LdwmYqTmO4iTseMPkcSb8AE&oq=findall+beautifulsoup+link+&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgQIABAKSgQIQRgASgQIRhgAUKMJWIITYOwhaAFwAXgAgAHbAYgBvgeSAQUwLjUuMZgBAKABAcgBCMABAQ&sclient=gws-wiz")
soup = BeautifulSoup(htmldata, 'html.parser')
links = []
for data in soup.find_all("a", href=True):
	links.append(data['href'])


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)
    

try:
         for link in links:
             print(link)
             print("----------over---------")
            #html = urlopen(link).read()
            #print(text_from_html(html))
	#print(type(text_from_html(html)))

except:
        print(e)
