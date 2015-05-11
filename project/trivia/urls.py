from django.conf.urls import include, url, patterns
from django.contrib import admin
from trivia.views import QuestionView,ChoicesView,GenreView

urlpatterns = patterns ('',

    url(r'^$', GenreView.as_view()),
    url(r'^questions/(?P<genre>[\w\-]+)/$', QuestionView.as_view()),
    url(r'^choices/(?P<artist>[\w\%]*?)/$', ChoicesView.as_view()),
)
