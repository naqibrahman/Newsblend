import requests
import json
import mysite.settings

def get_headlines():
    api_key = mysite.settings.NEWS_API_KEY
    url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=" + api_key
    r = requests.get(url)
    json_obj = r.json()
    articles = []
    for article in json_obj['articles']:
        articles.append(
            {
                "source_id": article['source']['id'],
                "title": article['title'],
                "url": article['url']
            }
        )
    return articles
