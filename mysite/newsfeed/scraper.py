from bs4 import BeautifulSoup
import requests
from temp_list import articles
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.poolmanager import PoolManager
#import ssl

# class MyAdapter(HTTPAdapter):
#     def init_poolmanager(self, connections, maxsize, block=False):
#         self.poolmanager = PoolManager(num_pools=connections,
#                                        maxsize=maxsize,
#                                        block=block,
#                                        ssl_version=ssl.PROTOCOL_TLSv1)

URLS = [ article["url"] for article in articles]
def scrape(url):
    try:
        mysession = requests.Session()
        #mysession.mount('https://', MyAdapter())
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        data = mysession.get(url,headers=headers).content
        soup = BeautifulSoup(data,"html.parser")
        ptags = soup.find_all('p');
        data = [str(p) for p in ptags]
        data = [ text.replace('\n','') for text in data]
    except KeyboardInterrupt:
       data = ["<h3>There was an error retrieving this site</h3>"]
       
    return data

def testrun():
    x = [ scrape(url) for url in URLS]
    text = ["".join(y)+"\n\n ARTICLE END \n\n" for y in x ]
    
    print(text)
    with open ('scrapings.text','w') as myf:
        myf.writelines(text)
#print(URLS[1])
#print(testrun())
