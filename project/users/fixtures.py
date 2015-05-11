import factory
from . import models

# from users.models import User

class UserFactory(factory.Factory):
    class Meta:
        model = models.User # imports for you

    username = 'stevepoly69'
    email = 'stevepoly69@snl.com'
    password='bigeffindict'
    about='I\'ll drink all your beers, I\'ll eat the last slice'
    points=10
