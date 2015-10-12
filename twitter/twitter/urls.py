
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^twitter_app/', include('twitter_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
