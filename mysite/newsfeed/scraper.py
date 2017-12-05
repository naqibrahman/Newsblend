from bs4 import BeautifulSoup
import requests
from temp_list import articles
#TODO: Error Handling

URLS = [ article["url"] for article in articles]
def scrape(url):
    try:
        mysession = requests.Session()
        data = mysession.get(url).content
        soup = BeautifulSoup(data,"html.parser")
        ptags = soup.find_all('p');
        data = [str(p) for p in ptags]
        data = [ text.replace('\n','') for text in data]
    except:
          data = ["There was an error retrieving this site"]
    return data

def testrun():
    x = [ scrape(url) for url in URLS]
    text = ["".join(y)+"\n\n ARTICLE END \n\n" for y in x ]
    
    print(text)
    with open ('scrapings.text','w') as myf:
        myf.writelines(text)
#print(URLS[1])
#print(testrun())
