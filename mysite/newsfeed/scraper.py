from bs4 import BeautifulSoup
import requests
from temp_list import articles
#TODO: Error Handling

URLS = [ article["url"] for article in articles]
def scrape(url):
    try:
        mysession = requests.Session()
        data = mysession.get(url).content
        soup = BeautifulSoup(data)
        ptags = soup.find_all('p');
        data = [p.contents[0] for p in ptags]
        data = [ text.replace('\n','') for text in data]
    except:
        data = ["There was an error retrieving this site"]
    return data

def testrun():
    return [ scrape(url) for url in URLS]
print(URLS[1]);
print(scrape(URLS[1]));
