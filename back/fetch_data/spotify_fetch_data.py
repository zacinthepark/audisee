import requests
import base64
import json
import pprint

# Get Spotify Token

client_id = 'aa0f99fe91aa41848d44a42b3b424583'
client_secret = 'd782f786c6ff4f43883343fd03ebaf8d'
endpoint = 'https://accounts.spotify.com/api/token'

encoded = base64.b64encode((f'{client_id}:{client_secret}').encode('utf-8')).decode('ascii')
headers = {'Authorization': f'Basic {encoded}'}
payload = {'grant_type': 'client_credentials'}
response = requests.post(endpoint, data=payload, headers=headers)
access_token = json.loads(response.text)['access_token']
headers = {'Authorization': f'Bearer {access_token}'}

# Fetch Music Genres Data

# music_genres_response = requests.get('https://api.spotify.com/v1/recommendations/available-genre-seeds', headers=headers)
# music_genres_response = json.loads(music_genres_response.text)

# music_genres_json = []
# for genre in music_genres_response['genres']:
#     music_genre_info = {'model': 'api.musicgenre'}
#     music_genre_info['fields'] = {}
#     music_genre_info['fields']['name'] = genre
#     music_genres_json.append(music_genre_info)
# pprint.pprint(music_genres_json)

# genres_type = ['acoustic', 'blues', 'classical', 'country', 'dance', 'disco', 'hip-hop', 'jazz', 'pop', 'k-pop', 'r-n-b', 'rock', 'reggae']
# genres_mood = ['ambient', 'club', 'chill', 'emo', 'groove', 'happy', 'holidays', 'party', 'rainy-day', 'road-trip', 'romance', 'sad', 'new-age', 'summer']
genres = [
    'pop', 'holidays', 'drum-and-bass', 
    'j-pop', 'soundtracks', 'anime', 
    'acoustic', 'piano', 'new-age',
    'rainy-day', 'classical', 'sad',
    'work-out', 'hip-hop', 'gospel',
    'comedy', 'happy', 
    'romance', 'r-n-b', 
    'classical', 'country', 'road-trip',
    'pop-film',
    'opera',
]
# genres_region = ['brazil', 'british', 'french', 'german', 'indian', 'iranian', 'j-pop', 'k-pop', 'latin', 'malay', 'pop', 'spanish', 'turkish']
# tracks_by_type_json = []
# tracks_by_mood_json = []
# tracks_by_region_json = []
tracks_json = []

# Make Tracks Data

for genre in genres:
    params = {
        'seed_genres': genre,
        'limit': 100,
    }
    response_music = requests.get('https://api.spotify.com/v1/recommendations', params=params, headers=headers)
    json_music = json.loads(response_music.text)
    # pprint.pprint(json_music)
    random_tracks_music = json_music['tracks']
    for random_track in random_tracks_music:
        music_info_by_type = {'model': 'api.music'}
        music_info_by_type['fields'] = {}

        track_genre = genre
        track_name = random_track['name']
        artist_name = random_track['artists'][0]['name']
        album_name = random_track['album']['name']
        cover_path_data = random_track['album']['images']
        if cover_path_data == []:
            cover_path = 'None'
        else:
            cover_path = random_track['album']['images'][1]['url']
        popularity = random_track['popularity']
        preview_url_data = random_track['preview_url']
        if preview_url_data == None:
            preview_url = 'None'
        else:
            preview_url = random_track['preview_url']
        music_info_by_type['fields']['track_genre'] = track_genre
        music_info_by_type['fields']['track_name'] = track_name
        music_info_by_type['fields']['artist_name'] = artist_name
        music_info_by_type['fields']['album_name'] = album_name
        music_info_by_type['fields']['cover_path'] = cover_path
        music_info_by_type['fields']['popularity'] = popularity
        music_info_by_type['fields']['preview_url'] = preview_url

        tracks_json.append(music_info_by_type)
# pprint.pprint(tracks_by_type_json)

with open('./api/fixtures/musics.json', 'w', encoding='UTF-8') as outfile:
    json.dump(tracks_json, outfile, indent=4, ensure_ascii=False)

# Make Tracks by Music Type Data

# for genre in genres_type:
#     params = {
#         'seed_genres': genre,
#         'limit': 10,
#     }
#     response_music = requests.get('https://api.spotify.com/v1/recommendations', params=params, headers=headers)
#     json_music = json.loads(response_music.text)
#     # pprint.pprint(json_music)
#     random_tracks_music = json_music['tracks']
#     for random_track in random_tracks_music:
#         music_info_by_type = {'model': 'api.music'}
#         music_info_by_type['fields'] = {}

#         track_genre = genre
#         track_name = random_track['name']
#         artist_name = random_track['artists'][0]['name']
#         album_name = random_track['album']['name']
#         cover_path_data = random_track['album']['images']
#         if cover_path_data == []:
#             cover_path = 'None'
#         else:
#             cover_path = random_track['album']['images'][1]['url']
#         popularity = random_track['popularity']
#         preview_url_data = random_track['preview_url']
#         if preview_url_data == None:
#             preview_url = 'None'
#         else:
#             preview_url = random_track['preview_url']
#         music_info_by_type['fields']['track_genre'] = track_genre
#         music_info_by_type['fields']['track_name'] = track_name
#         music_info_by_type['fields']['artist_name'] = artist_name
#         music_info_by_type['fields']['album_name'] = album_name
#         music_info_by_type['fields']['cover_path'] = cover_path
#         music_info_by_type['fields']['popularity'] = popularity
#         music_info_by_type['fields']['preview_url'] = preview_url
# #         # track_info = {
# #         #     'genre': genre,
# #         #     'track_name': track_name,
# #         #     'artist_name': artist_name,
# #         #     'album_name': album_name,
# #         #     'cover_path': cover_path,
# #         #     'popularity': popularity,
# #         #     'preview_url' : preview_url,
# #         # }
#         tracks_by_type_json.append(music_info_by_type)
# # pprint.pprint(tracks_by_type_json)

# with open('./api/fixtures/musics_by_type.json', 'w', encoding='UTF-8') as outfile:
#     json.dump(tracks_by_type_json, outfile, indent=4, ensure_ascii=False)

# Make Tracks by Mood Data

# for genre in genres_mood:
#     params = {
#         'seed_genres': genre,
#         'limit': 10,
#     }
#     response_music = requests.get('https://api.spotify.com/v1/recommendations', params=params, headers=headers)
#     json_music = json.loads(response_music.text)
#     random_tracks_music = json_music['tracks']
#     # pprint.pprint(random_tracks_music)
#     for random_track in random_tracks_music:
#         music_info_by_mood = {'model': 'api.music'}
#         music_info_by_mood['fields'] = {}

#         track_genre = genre
#         track_name = random_track['name']
#         artist_name = random_track['artists'][0]['name']
#         album_name = random_track['album']['name']
#         cover_path_data = random_track['album']['images']
#         if cover_path_data == []:
#             cover_path = 'None'
#         else:
#             cover_path = random_track['album']['images'][1]['url']
#         popularity = random_track['popularity']
#         preview_url_data = random_track['preview_url']
#         if preview_url_data == None:
#             preview_url = 'None'
#         else:
#             preview_url = random_track['preview_url']
#         music_info_by_mood['fields']['track_genre'] = track_genre
#         music_info_by_mood['fields']['track_name'] = track_name
#         music_info_by_mood['fields']['artist_name'] = artist_name
#         music_info_by_mood['fields']['album_name'] = album_name
#         music_info_by_mood['fields']['cover_path'] = cover_path
#         music_info_by_mood['fields']['popularity'] = popularity
#         music_info_by_mood['fields']['preview_url'] = preview_url
        
#         tracks_by_mood_json.append(music_info_by_mood)
# # pprint.pprint(tracks_by_mood_json)

# with open('./api/fixtures/musics_by_mood.json', 'w', encoding='UTF-8') as outfile:
#     json.dump(tracks_by_mood_json, outfile, indent=4, ensure_ascii=False)

# Make Tracks by Region Data

# for genre in genres_region:
#     params = {
#         'seed_genres': genre,
#         'limit': 50,
#     }
#     response_music = requests.get('https://api.spotify.com/v1/recommendations', params=params, headers=headers)
#     json_music = json.loads(response_music.text)
#     random_tracks_music = json_music['tracks']
#     for random_track in random_tracks_music:
#         track_name = random_track['name']
#         artist_name = random_track['artists'][0]['name']
#         cover_path = random_track['album']['images'][1]['url']
#         track_info = {
#             'genre': genre,
#             'title': track_name,
#             'artist': artist_name,
#             'cover_path': cover_path,
#         }
#         tracks_by_region_json.append(track_info)
# pprint.pprint(tracks_by_region_json)
