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
            # print(similar_artists_dict['response']['artists'][0]['name'])
            for artist in range(0, len(similar_artists_dict['response']['artists'])-1):
                print(similar_artists_dict['response']['artists'][artist]['name'])
                results_array.append(artist)
            return results_array

        else:
            print("No artists found.")
            return None

    def get_genre_artists(self, string):
        results_array = []
        search_result = requests.get(self.genre_artists_url + string)
        if search_result.json() != []:
            genre_artists_dict = search_result.json()
            for artist in range(0, len(genre_artists_dict['response']['artists'])-1):
                print(genre_artists_dict['response']['artists'][artist]['name'])
                results_array.append(artist)
            return results_array
        else:
            print("No artists found.")
            return None


    def get_artist_songs(self, string):
        results_array = []
        search_result = requests.get(self.artist_songs_url + string)
        if search_result.json() != []:
            artist_songs_dict = search_result.json()
            for song in range(0, len(artist_songs_dict['response']['songs'])-1):
                print(artist_songs_dict['response']['songs'][song]['title'])
                results_array.append(song)
            return results_array
        else:
            print("No songs found.")
            return None


    def get_artist_biographies(self, string):
        results_array = []
        search_result = requests.get(self.biographies_url + string)
        if search_result.json() != []:
            artist_biographies_dict = search_result.json()
            print(artist_biographies_dict['response']['biographies'][0]['text'])
            results_array.append(artist_biographies_dict['response']['biographies'][0]['text'])
            return results_array
        else:
            print("No biography found.")
            return None


e = EchoNest()
e.similar_artist_search('rainbow')
print()
e.get_genre_artists('rock')
print()
e.get_artist_songs('deeppurple')
print()
e.get_artist_biographies('blindfaith')
print()
