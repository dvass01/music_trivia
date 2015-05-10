from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns ('',

    url(r'^questions/(?P<genre>\w+)/$', QuestionView.as_view()),
    url(r'^choices/(P<user_choice>\d+)/$', ChoicesView.as_view()),
)
