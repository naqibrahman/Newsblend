from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'^$', views.index, name='index'),
    url(r'^$', views.newsfeed, name='newsfeed'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^news_page/(.*)/$', views.news_page, name='news_page')
]
