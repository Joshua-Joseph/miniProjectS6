# importing modules
import re
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time


# link for extracting html data
def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://www.google.com/search?q=set+default+python+interpreter+vscode&rlz=1C5CHFA_enIN895IN895&oq=set+default+python+i&aqs=chrome.2.69i57j0i512l7j0i22i30l2.12521j0j4&sourceid=chrome&ie=UTF-8")
soup = BeautifulSoup(htmldata, 'html.parser')
links = []
for data in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    links.append(
        (re.split(":(?=http)", data["href"].replace("/url?q=", "")))[0].split("&")[0])

# extracting the visible(on website) text


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


# text from each link overwrites the previous one therefore we need to pass the file before updation to the model
t1 = time.time()
for link in links:
    try:
        html = urlopen(link).read()
        f = open("demo.txt", "w")
        f.write(text_from_html(html))
        f.close()
        # pass this file to the model

    except Exception as e:
        f = open("demo.txt", "w")
        f.write(str(e))
        f.close()


t2 = time.time()
print(t2-t1)  # close to 30-35 s
