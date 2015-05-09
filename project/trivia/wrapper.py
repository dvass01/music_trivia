import requests
import json

class EchoNest:
    def __init__(self):
        self.similar_artists_url = 'http://developer.echonest.com/api/v4/artist/similar?api_key=L04DEV3NFMZOKDFKY&format=json&bucket=id:CAABOUD13216257FC7&limit=true&name='

        self.genre_artists_url = 'http://developer.echonest.com/api/v4/genre/artists?api_key=L04DEV3NFMZOKDFKY&format=json&results=5&bucket=hotttnesss&name='

        self.artist_songs_url = 'http://developer.echonest.com/api/v4/artist/songs?api_key=L04DEV3NFMZOKDFKY&format=json&results=15&name='

        self.biographies_url = 'http://developer.echonest.com/api/v4/artist/biographies?api_key=L04DEV3NFMZOKDFKY&format=json&results=1&start=0&license=cc-by-sa&name='


    # def get_artist_id(self):
    #     pass


    def similar_artist_search(self, string):
        results_array = []
        search_result = requests.get(self.similar_artists_url + string)
        if search_result.json() != []:
            similar_artists_dict =search_result.json()
            print(similar_artists_dict['response']['artists'][0]['name'])

        else:
            print("No artists found.")
            return None

    def get_genre_artists(self, string):
        results_array = []
        search_result = requests.get(self.genre_artists_url + string)
        print(search_result.json())

    def get_artist_songs(self, string):
        results_array = []
        search_result = requests.get(self.artist_songs_url + string)
        print(search_result.json())

    def get_artist_biographies(self, string):
        results_array = []
        search_result = requests.get(self.biographies_url + string)
        print(search_result.json())

e = EchoNest()
e.similar_artist_search('ledzeppelin')
# e.get_genre_artists('rock')
# e.get_artist_songs('ledzeppelin')
# e.get_artist_biographies('blindfaith')
