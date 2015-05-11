from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.db import models
from users.models import User
from users.forms import UserForm
from trivia.models import Genre
from trivia.wrapper import EchoNest

# Create your models here.

class GenreView(View):
    template_name = 'trivia/index.html'
    all_genres = Genre.objects.all()

    def get(self, request):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        return render(request, self.template_name, {'all_genres': self.all_genres, 'active_user': active_user})


class QuestionView(View):
    info_search = EchoNest()
    template_name = 'trivia/questions.html'
    context_dict = {}

    def get(self, request):
        artists_songs_dict = self.info_search.get_dict(genre_choice)
        





    def post(self, request):
        pass

class ChoicesView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class ResultsView(View):
    template_name = 'trivia/results.html'


    def get(self, request):
        pass
