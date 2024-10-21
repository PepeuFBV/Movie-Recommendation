import json
import requests
import pandas as pd
import re

# read the URL from the urls.txt file
with open('urls.txt', 'r') as file:
    line = file.readline().strip()
    url = line.split('send_url:')[1].strip()

movies = pd.read_csv('data/final_data/movies_full.csv')

# remove the unused columns
if 'endYear' in movies.columns:
    movies = movies.drop(columns=['endYear'])
if 'imdb_id' in movies.columns:
    movies = movies.drop(columns=['imdb_id'])
if 'tmdb_id' in movies.columns:
    movies = movies.drop(columns=['tmdb_id'])

for column in movies.columns:
    print(column)

# dictionary to map old column names to new ones
column_rename_map = {
    'movie_id': 'modelId',
    'primaryTitle': 'title',
    'originalTitle': 'alternativeTitle',
    'original_language': 'language',
    'overview': 'description',
    'genres': 'genre',
    'startYear': 'releaseDate',
    'runtimeMinutes': 'duration',
    'isAdult': 'rating',
    'rating': 'score',
    'backdrop_path': 'posterUrl',
    'video_key': 'videoUrl',
    'poster_path': 'imageUrl'
}

# rename columns if the dictionary is not empty
if column_rename_map:
    movies = movies.rename(columns=column_rename_map)

# reorder columns
movies = movies[
    ['modelId', 'title', 'alternativeTitle', 'language', 'description', 'genre', 'releaseDate', 'duration',
     'score', 'rating', 'directors', 'actors', 'posterUrl', 'videoUrl', 'imageUrl']]

# check if 'directors', 'actors', and 'genre' columns exist and convert them to lists of strings if they do
if 'directors' in movies.columns:
    movies['directors'] = movies['directors'].apply(lambda x: x.split(',') if pd.notnull(x) else [])
if 'actors' in movies.columns:
    movies['actors'] = movies['actors'].apply(lambda x: x.split(',') if pd.notnull(x) else [])
if 'genre' in movies.columns:
    movies['genre'] = movies['genre'].apply(lambda x: x.split(',') if pd.notnull(x) else [])

# convert 'runtime' to integer if it exists
if 'duration' in movies.columns:
    movies['duration'] = movies['duration'].astype(int)

# remove the leading backslash from 'posterUrl', 'imageUrl' and 'videoUrl' if they exist
if 'posterUrl' in movies.columns:
    movies['posterUrl'] = movies['posterUrl'].str.lstrip('\\')
if 'imageUrl' in movies.columns:
    movies['imageUrl'] = movies['imageUrl'].str.lstrip('\\')
if 'videoUrl' in movies.columns:
    movies['videoUrl'] = movies['videoUrl'].str.lstrip('\\')

# make the rating a string of the boolean value
if 'rating' in movies.columns:
    movies['rating'] = movies['rating'].astype(str)

# format to 2 decimal places
# if 'score' in movies.columns:
#     movies['rating'] = movies['rating'].apply(lambda x: "{:.2f}".format(float(x)))

# make the 'releaseDate' a string
if 'releaseDate' in movies.columns:
    movies['releaseDate'] = movies['releaseDate'].astype(str)

# convert 'releaseDate' to datetime and format it as MM/DD/YYYY
if 'releaseDate' in movies.columns:
    movies['releaseDate'] = pd.to_datetime(movies['releaseDate'], errors='coerce').dt.strftime('%Y-%m-%d')


def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)


# Apply the function to the relevant columns in your DataFrame
for column in movies.select_dtypes(include=[object]).columns:
    movies[column] = movies[column].apply(lambda x: remove_non_ascii(x) if isinstance(x, str) and pd.notnull(x) else x)


def login() -> str:
    route = '/user/auth/login'

    payload = {
        'email': 'admin@gmail.com',
        'password': 'admin123!'
    }

    response = requests.post(url + route, json=payload)
    return response.json()['token']


def send_data(r_token: str, payload: str, print_response: bool = True):
    route = 'movies/save_all'

    headers = {
        'Authorization': 'Bearer ' + r_token,
        'Content-Type': 'application/json'
    }

    response = requests.post(url + route, headers=headers, data=payload)
    if print_response:
        print(response)


def send_movies_in_chunks(movies_df, chunk_size=1000):
    token = login()
    num_chunks = len(movies_df) // chunk_size + (1 if len(movies_df) % chunk_size != 0 else 0)

    for i in range(num_chunks):
        chunk = movies_df.iloc[i * chunk_size:(i + 1) * chunk_size]
        data = chunk.to_json(orient='records')

        # Ensure proper JSON encoding
        try:
            data = json.dumps(json.loads(data), ensure_ascii=False)
        except json.JSONDecodeError as e:
            print(f"JSON encoding error: {e}")
            continue

        send_data(token, data, print_response=False)
        print(f"Sent movie {i + 1}/{num_chunks}")


def send_first_movie():
    token = login()
    movie = movies.head(1).to_json(orient='records')
    movie = json.dumps(json.loads(movie), ensure_ascii=False)
    movie = movie.encode('utf-8').decode('unicode_escape')  # fix the encoding issues
    print(movie)
    send_data(token, movie)


# send movies in chunks of 100
send_movies_in_chunks(movies, chunk_size=100)
# send_first_movie()
