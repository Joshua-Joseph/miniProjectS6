# import module
import re
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# link for extracting html data
def getdata(url):
	r = requests.get(url)
	return r.text

htmldata = getdata("https://www.google.com/search?q=russsia&oq=russsia+&aqs=chrome..69i57.2172j0j9&sourceid=chrome&ie=UTF-8")
soup = BeautifulSoup(htmldata, 'html.parser')
links = []
for data in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
	links.append((re.split(":(?=http)",data["href"].replace("/url?q=","")))[0].split("&")[0])


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
    

for link in links:
    try:
            #print(link)
            html = urlopen(link).read()
            print(text_from_html(html))
            print("----------------OVER-----------------")
	#print(type(text_from_html(html)))

    except Exception as e:
        print(e)
