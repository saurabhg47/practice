from django.conf.urls import include, url, patterns
from django.contrib import admin
from polls.views import sample_sender, call_no, answer_url



urlpatterns = patterns('',url(r'^send/msg', sample_sender),
						url(r'^call', call_no),
						url(r'^answer', answer_url))
