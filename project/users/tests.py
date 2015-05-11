from django.test import TestCase,Client
from users.fixtures import UserFactory
from users.models import User
# Create your tests here.
from django.test import TestCase

class TestClient(TestCase):
    def setUp(self):
        self.client = Client()
        # self.user = UserFactory()
        # self.steve = UserFactory(username='stevepoly69')

    def test_getrequests(self):
        res = self.client.get('/users')
        # self.assertEqual(res.status_code, 200) # page works
        # self.assertEqual(res.context['user'], 'user') # test the dict sent to the template
        self.assertEqual(res.request['REQUEST_METHOD'], "GET")
        # self.assertIn(self.client, res.context['clients'])
        # self.assertTrue(self.steven.name in str(res.content))

class TestUser(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_user_attributes(self):
        self.assertEqual(self.user.username, "stevepoly69")
        self.assertEqual(self.user.password, "bigeffindict")
        self.assertEqual(self.user.email, "stevepoly69@snl.com")
        self.assertEqual(self.user.about, "I\'ll drink all your beers, I\'ll eat the last slice")

    def test_index(self):
        res = self.client.get('/users')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.request['REQUEST_METHOD'], "GET")
        self.assertIn(self.user, res.context['users'])
        self.assertTrue(self.user.usernamename in str(res.content))
