from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm

# Create your models here.

class User(models.Model):
    def validate_username(submitted_username):
        if len(User.objects.filter(username=submitted_username)) > 0:
            raise ValidationError("This username is already taken.")

    def validate_password(submitted_password):
        if len(submitted_password) < 7:
            raise ValidationError("Password must be at least 7 characters in length.")

    username = models.CharField(max_length=255,unique=True,validators=[validate_username])
    password = models.CharField(max_length=255,validators=[validate_password])
    created_at = models.DateTimeField(auto_now_add=True)
    about = models.TextField(default='[user description]')
    points = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    win_percentage = models.CharField(max_length=254, default=0)

    def calculate_win_percentage(self):
        new_win_percentage = float((self.points/self.games_played)*100)
        return new_win_percentage
