from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.db import models
from users.models import User
from users.forms import UserForm
from trivia.models import Genre,Question
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
            if question_dict:
                all_artists = []
                for row in question_dict:
                    slugged_artist = row[0].replace(" ","_")
                    all_artists.append(slugged_artist)

                answer_pair = random.choice(question_dict)
                correct_artist = answer_pair[0].replace(" ","_")
                correct_song = answer_pair[1].replace(" ","_")

                print(correct_song)
                print(correct_artist)
                question_text = "Which artist performed {}?".format(correct_song)

                question = Question.objects.create(user_id=active_user[0],answer=correct_artist,question_text=question_text,choice_1=all_artists[0],choice_2=all_artists[1],choice_3=all_artists[2],choice_4=all_artists[3])

                request.session['question_text'] = question_text

                return render(request,self.template_name, {'active_user':active_user[0],'all_artists':all_artists, 'correct_artist':correct_artist, 'correct_song':correct_song,'question_text':question_text})
            return redirect('/trivia')
        return redirect('/users/login')


    def post(self, request, artist):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)[0]
        question_text = request.session.get('question_text')
        question = Question.objects.filter(question_text=question_text)[0]
        artist.replace('%20',' ')
        active_user.games_played += 1
        active_user.save()
        if question.answer == artist:
            active_user.points += 1
            active_user.win_percentage = active_user.calculate_win_percentage()
            active_user.save()
            return render(request,self.template_name,{'result':'Correct!','active_user':active_user})
        return render(request,self.template_name,{'result':'Nope.','active_user':active_user})


class ChoicesView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class ResultsView(View):
    template_name = 'trivia/results.html'


    def get(self, request):
        pass
