from django.conf.urls import include, url,patterns
from django.contrib import admin
from users.views import RegisterView, IndexView,LoginView,UserView,LogoutView
from django.views.generic import View


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',IndexView.as_view()),

    url(r'^register$', RegisterView.as_view()),

    url(r'^login$', LoginView.as_view()),

    url(r'^logout$',LogoutView.as_view()),

    url(r'^(?P<username>[\w\-]+)$', UserView.as_view()),
)
