import requests
import json
import collections
from collections import defaultdict

class EchoNest:
    def __init__(self):
        self.similar_artists_url = 'http://developer.echonest.com/api/v4/artist/similar?api_key=L04DEV3NFMZOKDFKY&format=json&bucket=id:CAABOUD13216257FC7&limit=true&name='

        self.genre_artists_url = 'http://developer.echonest.com/api/v4/genre/artists?api_key=L04DEV3NFMZOKDFKY&format=json&results=15&bucket=hotttnesss&name='

        self.artist_songs_url = 'http://developer.echonest.com/api/v4/artist/songs?api_key=L04DEV3NFMZOKDFKY&format=json&results=25&name='

        self.biographies_url = 'http://developer.echonest.com/api/v4/artist/biographies?api_key=L04DEV3NFMZOKDFKY&format=json&results=1&start=0&license=cc-by-sa&name='


    # def get_artist_id(self):
    #     pass


    def similar_artist_search(self, name):
        results_array = []
        search_result = requests.get(self.similar_artists_url + name)
        if search_result.json() != []:
            similar_artists_dict =search_result.json()
            # print(similar_artists_dict['response']['artists'][0]['name'])
            for artist in range(0, len(similar_artists_dict['response']['artists'])-1):
                # print(similar_artists_dict['response']['artists'][artist]['name'])
                results_array.append(similar_artists_dict['response']['artists'][artist]['name'])
            return results_array

        else:
            # print("No artists found.")
            return None

    def get_genre_artists(self, genre):
        results_array = []
        search_result = requests.get(self.genre_artists_url + genre)
        if search_result.json() != []:
            genre_artists_dict = search_result.json()
            for artist in range(0, len(genre_artists_dict['response']['artists'])-1):
                # print(genre_artists_dict['response']['artists'][artist]['name'])
                results_array.append(genre_artists_dict['response']['artists'][artist]['name'])
            return results_array
        else:
            # print("No artists found.")
            return None


    def get_artist_songs(self, name):
        results_array = []
        search_result = requests.get(self.artist_songs_url + name)
        if search_result.json() != []:
            artist_songs_dict = search_result.json()
            for song in range(0, len(artist_songs_dict['response']['songs'])-1):
                # print(artist_songs_dict['response']['songs'][song]['title'])
                results_array.append(artist_songs_dict['response']['songs'][song]['title'])
            return results_array
        else:
            # print("No songs found.")
            return None


    def get_artist_biographies(self, name):
        results_array = []
        search_result = requests.get(self.biographies_url + name)
        if search_result.json() != []:
            artist_biographies_dict = search_result.json()
            # print(artist_biographies_dict['response']['biographies'][0]['text'])
            results_array.append(artist_biographies_dict['response']['biographies'][0]['text'])
            return results_array
        else:
            # print("No biography found.")
            return None


    def get_dict(self, genre):
        # print(e.get_genre_artists('rock'))
        artist_list = e.get_genre_artists(genre)
        artists_songs = []
        for artist in artist_list:
            # print(e.get_artist_songs(artist))
            song_list = e.get_artist_songs(artist)
            for song in song_list:
                artists_songs.append([artist, song])
        # print()
        # for row in artists_songs:
        #     print(row)
        # print()
        d = defaultdict(list)
        for k, v in artists_songs:
            d[k].append(v)
        # for k, v in d.items():
        #     print(k, v)
        #     print()
        return d.items()


# e = EchoNest()
# e.similar_artist_search('rainbow')
# print()
# e.get_genre_artists('rock')
# print()
# e.get_artist_songs('deeppurple')
# print()
# e.get_artist_biographies('blindfaith')
# print()
# print(e.get_dict('rock'))
