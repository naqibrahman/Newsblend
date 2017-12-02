from bs4 import BeautifulSoup
import requests
from temp_list import articles

URLS = [ article["url"] for article in articles]
def scrape(url):
    mysession = requests.Session()
    data = mysession.get(url).content
    soup = BeautifulSoup(data)
    ptags = soup.find_all('p');
    data = [p.contents[0] for p in ptags]
    data = [ text.replace('\n','') for text in data]
    return data


