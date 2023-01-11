import json
import requests
import pprint
API_KEY = '512acd9151aae945ad5408b2647daba0'
# page = 5
# MOVIE_URL_1 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=1&include_adult=true'
# MOVIE_URL_2 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=2&include_adult=true'
# MOVIE_URL_3 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=3&include_adult=true'
# MOVIE_URL_4 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=4&include_adult=true'
# MOVIE_URL_5 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=5&include_adult=true'
# MOVIE_URL_6 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=6&include_adult=true'
# MOVIE_URL_7 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=7&include_adult=true'
# MOVIE_URL_8 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=8&include_adult=true'
# MOVIE_URL_9 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=9&include_adult=true'
# MOVIE_URL_10 = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=ko-KR&query=a&page=10&include_adult=true'

MOVIE_URL_1 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=1'
MOVIE_URL_2 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=2'
MOVIE_URL_3 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=3'
MOVIE_URL_4 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=4'
MOVIE_URL_5 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=5'
MOVIE_URL_6 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=6'
MOVIE_URL_7 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=7'
MOVIE_URL_8 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=8'
MOVIE_URL_9 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=9'
MOVIE_URL_10 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=10'
MOVIE_URL_11 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=11'
MOVIE_URL_12 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=12'
MOVIE_URL_13 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=13'
MOVIE_URL_14 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=14'
MOVIE_URL_15 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=15'
MOVIE_URL_16 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=16'
MOVIE_URL_17 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=17'
MOVIE_URL_18 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=18'
MOVIE_URL_19 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=19'
MOVIE_URL_20 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=20'
MOVIE_URL_21 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=20'
MOVIE_URL_22 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=20'
MOVIE_URL_23 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=20'
MOVIE_URL_24 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=20'
MOVIE_URL_25 = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page=20'
GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR'

movie_genres_response = requests.get(GENRE_URL)
movie_genres_response = json.loads(movie_genres_response.text)


# Make Movie Genres Fixture File
movie_genres_json = []
for genre in movie_genres_response['genres']:
    movie_genre_info = {'model': 'api.genre'}
    movie_genre_info['id'] = genre['id']
    movie_genre_info['fields'] = {}
    movie_genre_info['fields']['name'] = genre['name']
    movie_genres_json.append(movie_genre_info)
pprint.pprint(movie_genres_json)

with open('./api/fixtures/movie_genres.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movie_genres_json, outfile, indent=4, ensure_ascii=False)


# Fetch Movie Genres Data

# genre_infos = []
# for genre in movie_genres_response['genres']:
#     genre_mapping_dict = {}
#     genre_mapping_dict[str(genre['id'])] = genre['name']
#     genre_infos.append(genre_mapping_dict)
# # pprint.pprint(genre_infos)
# genre_ids_and_names = {}
# for genre_info in genre_infos:
#     items = genre_info.items()
#     for item in items:
#         genre_ids_and_names[item[0]] = item[1]
# pprint.pprint(genre_ids_and_names)


# Fetch Movies Data

# 1

movies_response_1 = requests.get(MOVIE_URL_1)
movies_response_1 = json.loads(movies_response_1.text)
# pprint.pprint(movies_response_1)

movies_json_1 = []
for movie in movies_response_1['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_1.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_1.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_1, outfile, indent=4, ensure_ascii=False)

# 2

movies_response_2 = requests.get(MOVIE_URL_2)
movies_response_2 = json.loads(movies_response_2.text)
# pprint.pprint(movies_response)

movies_json_2 = []
for movie in movies_response_2['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_2.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_2.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_2, outfile, indent=4, ensure_ascii=False)


movies_response_3 = requests.get(MOVIE_URL_3)
movies_response_3 = json.loads(movies_response_3.text)
# pprint.pprint(movies_response)

# 3

movies_json_3 = []
for movie in movies_response_3['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_3.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_3.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_3, outfile, indent=4, ensure_ascii=False)


movies_response_4 = requests.get(MOVIE_URL_4)
movies_response_4 = json.loads(movies_response_4.text)
# pprint.pprint(movies_response)

# 4

movies_json_4 = []
for movie in movies_response_4['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_4.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_4.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_4, outfile, indent=4, ensure_ascii=False)

# 5

movies_response_5 = requests.get(MOVIE_URL_5)
movies_response_5 = json.loads(movies_response_5.text)
# pprint.pprint(movies_response)

movies_json_5 = []
for movie in movies_response_5['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_5.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_5.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_5, outfile, indent=4, ensure_ascii=False)

# 6

movies_response_6 = requests.get(MOVIE_URL_6)
movies_response_6 = json.loads(movies_response_6.text)
# pprint.pprint(movies_response)

movies_json_6 = []
for movie in movies_response_6['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_6.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_6.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_6, outfile, indent=4, ensure_ascii=False)

# 7

movies_response_7 = requests.get(MOVIE_URL_7)
movies_response_7 = json.loads(movies_response_7.text)
# pprint.pprint(movies_response)

movies_json_7 = []
for movie in movies_response_7['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_7.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_7.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_7, outfile, indent=4, ensure_ascii=False)

# 8

movies_response_8 = requests.get(MOVIE_URL_8)
movies_response_8 = json.loads(movies_response_8.text)
# pprint.pprint(movies_response)

movies_json_8 = []
for movie in movies_response_8['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_8.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_8.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_8, outfile, indent=4, ensure_ascii=False)

# 9

movies_response_9 = requests.get(MOVIE_URL_9)
movies_response_9 = json.loads(movies_response_9.text)
# pprint.pprint(movies_response)

movies_json_9 = []
for movie in movies_response_9['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_9.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_9.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_9, outfile, indent=4, ensure_ascii=False)

# 10

movies_response_10 = requests.get(MOVIE_URL_10)
movies_response_10 = json.loads(movies_response_10.text)
# pprint.pprint(movies_response)

movies_json_10 = []
for movie in movies_response_10['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_10.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_10.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_10, outfile, indent=4, ensure_ascii=False)

# 11

movies_response_11 = requests.get(MOVIE_URL_11)
movies_response_11 = json.loads(movies_response_11.text)
# pprint.pprint(movies_response)

movies_json_11 = []
for movie in movies_response_11['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_11.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_11.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_11, outfile, indent=4, ensure_ascii=False)

# 12

movies_response_12 = requests.get(MOVIE_URL_12)
movies_response_12 = json.loads(movies_response_12.text)
# pprint.pprint(movies_response)

movies_json_12 = []
for movie in movies_response_12['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_12.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_12.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_12, outfile, indent=4, ensure_ascii=False)

# 13

movies_response_13 = requests.get(MOVIE_URL_13)
movies_response_13 = json.loads(movies_response_13.text)
# pprint.pprint(movies_response)

movies_json_13 = []
for movie in movies_response_13['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_13.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_13.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_13, outfile, indent=4, ensure_ascii=False)

# 14

movies_response_14 = requests.get(MOVIE_URL_14)
movies_response_14 = json.loads(movies_response_14.text)
# pprint.pprint(movies_response)

movies_json_14 = []
for movie in movies_response_14['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_14.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_14.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_14, outfile, indent=4, ensure_ascii=False)

# 15

movies_response_15 = requests.get(MOVIE_URL_15)
movies_response_15 = json.loads(movies_response_15.text)
# pprint.pprint(movies_response)

movies_json_15 = []
for movie in movies_response_15['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_15.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_15.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_15, outfile, indent=4, ensure_ascii=False)

# 16

movies_response_16 = requests.get(MOVIE_URL_16)
movies_response_16 = json.loads(movies_response_16.text)
# pprint.pprint(movies_response)

movies_json_16 = []
for movie in movies_response_16['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_16.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_16.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_16, outfile, indent=4, ensure_ascii=False)

# 17

movies_response_17 = requests.get(MOVIE_URL_17)
movies_response_17 = json.loads(movies_response_17.text)
# pprint.pprint(movies_response)

movies_json_17 = []
for movie in movies_response_17['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_17.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_17.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_17, outfile, indent=4, ensure_ascii=False)

# 18

movies_response_18 = requests.get(MOVIE_URL_18)
movies_response_18 = json.loads(movies_response_18.text)
# pprint.pprint(movies_response)

movies_json_18 = []
for movie in movies_response_18['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_18.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_18.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_18, outfile, indent=4, ensure_ascii=False)

# 19

movies_response_19 = requests.get(MOVIE_URL_19)
movies_response_19 = json.loads(movies_response_19.text)
# pprint.pprint(movies_response)

movies_json_19 = []
for movie in movies_response_19['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_19.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_19.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_19, outfile, indent=4, ensure_ascii=False)

# 20

movies_response_20 = requests.get(MOVIE_URL_20)
movies_response_20 = json.loads(movies_response_20.text)
# pprint.pprint(movies_response)

movies_json_20 = []
for movie in movies_response_20['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_20.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_20.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_20, outfile, indent=4, ensure_ascii=False)

# 21

movies_response_21 = requests.get(MOVIE_URL_21)
movies_response_21 = json.loads(movies_response_21.text)
# pprint.pprint(movies_response)

movies_json_21 = []
for movie in movies_response_21['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_21.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_21.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_21, outfile, indent=4, ensure_ascii=False)

# 22

movies_response_22 = requests.get(MOVIE_URL_22)
movies_response_22 = json.loads(movies_response_22.text)
# pprint.pprint(movies_response)

movies_json_22 = []
for movie in movies_response_22['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_22.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_22.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_22, outfile, indent=4, ensure_ascii=False)

# 23

movies_response_23 = requests.get(MOVIE_URL_23)
movies_response_23 = json.loads(movies_response_23.text)
# pprint.pprint(movies_response)

movies_json_23 = []
for movie in movies_response_23['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_23.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_23.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_23, outfile, indent=4, ensure_ascii=False)

# 24

movies_response_24 = requests.get(MOVIE_URL_24)
movies_response_24 = json.loads(movies_response_24.text)
# pprint.pprint(movies_response)

movies_json_24 = []
for movie in movies_response_24['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_24.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_24.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_24, outfile, indent=4, ensure_ascii=False)

# 25

movies_response_25 = requests.get(MOVIE_URL_25)
movies_response_25 = json.loads(movies_response_25.text)
# pprint.pprint(movies_response)

movies_json_25 = []
for movie in movies_response_25['results']:
    movie_info = {'model': 'api.movie'}
    # movie_info['id'] = movie.pop('id')
    # movie_info['fields'] = movie
    movie_info['fields'] = {}
    movie_info['fields']['genre_ids'] = movie['genre_ids']
    movie_info['fields']['title'] = movie['title']
    movie_info['fields']['overview'] = movie['overview']
    movie_info['fields']['release_date'] = movie['release_date']
    movie_info['fields']['poster_path'] = movie['poster_path']
    movie_info['fields']['popularity'] = movie['popularity']
    movie_info['fields']['vote_count'] = movie['vote_count']
    movie_info['fields']['vote_average'] = movie['vote_average']

    # genres_list = []
    # genre_ids = movie['genre_ids']
    # items = genre_ids_and_names.items()
    # for item in items:
    #     for genre_id in genre_ids:
    #         if str(genre_id) == item[0]:
    #             genres_list.append(item[1])
    # if genres_list == []:
    #     genres_list.append('일반')
    # movie_info['fields']['genres'] = genres_list

    movies_json_25.append(movie_info)
# pprint.pprint(movies_json)

with open('./api/fixtures/movies_25.json', 'w', encoding='UTF-8') as outfile:
    json.dump(movies_json_25, outfile, indent=4, ensure_ascii=False)
