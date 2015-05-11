import requests
import json
import collections
from collections import defaultdict
import random

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
<<<<<<< HEAD
            try:
                for song in range(len(artist_songs_dict['response']['songs'])-1):
                    # print(artist_songs_dict['response']['songs'][song]['title'])
                    results_array.append(artist_songs_dict['response']['songs'][song]['title'])
            except KeyError:
                print('wait to execute again')
=======
            # print(artist_songs_dict['response'])
            for song in range(len(artist_songs_dict['response']['songs'])-1):
                # print(artist_songs_dict['response']['songs'][song]['title'])
                results_array.append(artist_songs_dict['response']['songs'][song]['title'])
>>>>>>> 722e88ed09ea111614f1142a348618ebb3e2dcfb
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
        e = EchoNest()
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
        # takes list of lists of artist and song and creates dict_items
        # object of tuples of artist and a list of their songs
        d = defaultdict(list)
        # print(artists_songs)
        for k, v in artists_songs:
            d[k].append(v)
        # for k, v in d.items():
        #     print(k, v)
        #     print()
        # print(d.items())
        return_list = list(d.items())
        return return_list

    def get_random_artist_songs(self, artists_songs_list):
        random_artist_songs = []
        # grabbing 4 artist songs tuples at random
        random_artists = random.sample(artists_songs_list, 4)

        for artist_song in random_artists:
            # grabbing 1 song from list in 2nd index of artist_song tuple
            random_song = random.sample(artist_song[1], 1)
            # first - random song is list of length 1
            random_artist_songs.append((artist_song[0], random_song[0]))
        return random_artist_songs


if __name__ == '__main__':
    pass

    # e = EchoNest()

    # print(e.get_artist_songs('radiohead'))

# e.similar_artist_search('rainbow')
# print()
# e.get_genre_artists('rock')
# print()
# e.get_artist_songs('deeppurple')
# print()
# e.get_artist_biographies('blindfaith')
# print()
# print(e.get_dict('rock'))
    # print(e.get_random_artist_songs(e.get_dict('rock')))
