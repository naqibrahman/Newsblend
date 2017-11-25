import requests
import mysite.settings

def get_headlines():
    api_key = mysite.settings.NEWS_API_KEY
    url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=" + api_key
    r = requests.get(url)
    print r.json()