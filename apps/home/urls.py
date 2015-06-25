from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.home.views',
	url(r'^$','view_index' ,name="home"),
	url(r'^login/$','view_login',name="login"),
	url(r'^logout/$','view_logout',name="logout"),
	url(r'^catalogos/$','view_cats',name="vista_catalogos"),
)