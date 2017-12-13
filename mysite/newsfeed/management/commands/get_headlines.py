from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from django_redis import get_redis_connection
import requests
import json
import mysite.settings
from newsfeed.models import Source, Article

class Command(BaseCommand):
    help = "Retrieves most recent top headlines from News API"

    def handle(self, *args, **options):
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

            source = Source.objects.filter(source_id=source_id)
            count = source.count()
            if count == 0:
                source_object= Source(source_id=source_id, source_name=source_name)
                source_object.save()

            article_count = Article.objects.filter(article_name=title).count()
            if article_count == 0:
                article_object = Article(article_name=title)
                article_source = Source.objects.get(source_id=source_id) 
                article_object.source = article_source
                article_object.save()

            article_id = Article.objects.get(article_name=title).article_id
            articles.append(json.dumps(
                    {
                        "source_id": source_id,
                        "title": title,
                        "url": url,
                        "id":article_id,
                        "source_bias": float(Source.objects.get(source_id=source_id).score_average)
                    }
                )
            )
        """
        TODO: Sort articles based on source bias score before returning
        """
        self.stdout.write(self.style.SUCCESS('Successfully retrieved headlines'))
        r = get_redis_connection("default")
        r.delete("articles")
        r.lpush("articles", *articles)