from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns ('',
    url(r'^trivia/', include('trivia.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
