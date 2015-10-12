from django.contrib import admin

from .models import USER, FOLLOWER, TWEET, FOLLOWING

admin.site.register(USER)
admin.site.register(FOLLOWER)
admin.site.register(TWEET)
admin.site.register(FOLLOWING)
# Register your models here.
