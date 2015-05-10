from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_name = models.CharField(max_length=8)

class Question(models.Model):
    user_id = models.ForeignKey('users.User')
    question_text = models.CharField(max_length=100)
    choice_1 = models.CharField(max_length=100)
    choice_2 = models.CharField(max_length=100)
    choice_3 = models.CharField(max_length=100)
    choice_4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    user_answer = models.IntegerField(null=True)

