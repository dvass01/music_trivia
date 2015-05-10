from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns ('',

    url(r'^trivia/questions/(?P<genre>\d+)/$', QuestionView.as_view()),
    url(r'^trivia/questions/(?P<artists>\d+)/$', QuestionView.as_view()),
    url(r'^trivia/questions/(?P<songs>\d+)/$', QuestionView.as_view()),

)
