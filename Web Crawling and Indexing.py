import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

visited=set()

def crawl(url,depth=1):

    if depth==0 or url in visited:
        return

    visited.add(url)

    try:
        r=requests.get(url)
        soup=BeautifulSoup(r.text,"html.parser")

        print("Crawling:",url)

        for link in soup.find_all("a",href=True):
            next_url=urljoin(url,link["href"])
            crawl(next_url,depth-1)

        time.sleep(1)

    except:
        pass


crawl("https://wikipedia.org",1)
