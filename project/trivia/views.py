from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.db import models
from users.models import User
from users.forms import UserForm
from trivia.models import Genre
from trivia.wrapper import EchoNest
import random
from random import sample,choice
# Create your models here.

class GenreView(View):
    template_name = 'trivia/index.html'
    all_genres = Genre.objects.all()

    def get(self, request):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        if active_user:
            return render(request, self.template_name, {'all_genres': self.all_genres, 'active_user': active_user[0]})
        return redirect('/users/login')

class QuestionView(View):
    info_search = EchoNest()
    template_name = 'trivia/questions.html'

    def get(self,request,genre):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        artists_songs_dict = self.info_search.get_dict(genre)

        if active_user:
            question_dict = self.info_search.get_random_artist_songs(self.info_search.get_dict(genre))
            all_artists=[]
            for row in question_dict:
                all_artists.append(row[0])
                answer_pair = random.choice(question_dict)
                correct_artist=answer_pair[0]
                correct_song=answer_pair[1]
            return render(request,self.template_name, {'active_user':active_user[0],'all_artists':all_artists,'correct_artist':correct_artist,'correct_song':correct_song})
        return redirect('/users/login')


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
