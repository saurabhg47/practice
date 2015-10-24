from django.conf.urls import include, url, patterns
from django.contrib import admin
from . import views
# from polls.views import sample_sender, call_no, answer_url


urlpatterns = [url(r'^$', views.index, name='index'),
			   url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
			   # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
			   # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
			   ]
# urlpatterns = patterns('',url(r'^send/msg', sample_sender),
# 						url(r'^call', call_no),
# 						url(r'^answer', answer_url))
