from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'^$', views.index, name='index'),
    url(r'^$', views.newsfeed, name='newsfeed'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^news_page/(.*)/$', views.news_page, name='news_page'),
	url(r'^article/(?P<articleId>\w{0,50})/$', views.article, name='article'),
	url(r'^createbiasscore/$', views.create_bias_score, name='create_bias_score')
]
