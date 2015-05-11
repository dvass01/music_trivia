from django.test import TestCase,Client

# Create your tests here.
from django.test import TestCase

class TestClient(TestCase):
    def setUp(self):
        self.client = Client()

    def test_getrequests(self):
        res = self.client.get('/users')
        print(res.status_code)
        self.assertEqual(res.status_code, 200) # page works
        self.assertEqual(res.context['user'], 'user') # test the dict sent to the template

class TestUser(TestCase):
    def setUp(self):
        self.user = User()

        def test_name(self):
            self.assertEqual(user.name, "Steve Polykronopolous")
