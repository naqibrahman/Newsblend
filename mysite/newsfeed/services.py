import requests
import json
import mysite.settings
from newsfeed.models import Source, Article

def get_headlines():
    api_key = mysite.settings.NEWS_API_KEY
    url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=" + api_key
    r = requests.get(url)
    json_obj = r.json()
    articles = []
    for article in json_obj['articles']:
        source_id = article['source']['id']
        source_name = article['source']['name']
        title = article['title']
        url = article['url']

        count = Source.objects.filter(source_id=source_id).count()
        if count == 0:
            source = Source(source_id=source_id, source_name=source_name)
            source.save()
         
        articles.append(
            {
                "source_id": source_id,
                "title": title,
                "url": url
            }
        )
    return articles
