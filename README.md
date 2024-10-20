# Movie-Recommendation

This repository focuses on developing a movie recommendation algorithm based on scores, aiming to suggest titles to users based on their previous ratings and liking's. The goal of this system is to identify which movies or series a user is likely to enjoy, assigning a score to each title based on their behavior and preferences.

By comparing the performance of these algorithms in the context of personalized recommendations, we can find the best model to increase user satisfaction on streaming platforms. The findings of this study could contribute to optimizing content delivery and production, as well as significantly improving the user experience in modern entertainment environments. Therefore, the development of an efficient recommendation engine is essential to elevate the level of user engagement.

Models such as Matrix Factorization algorithms (SVD, SVDpp, NMF), the Slope One algorithm and Co-Clustering, are used to predict the scores of movies and series. The data used in this study is the [MovieLens](https://grouplens.org/datasets/movielens/20m/) dataset, which contains information about user ratings and movie titles.

The repository also contains a script to fetch the remaining necessary data from The Movie Database (TMDb) API, such as movie genres, release dates, trailer links and other relevant information. The data is then preprocessed and saved in a CSV file to be used in the main application developed for using this project [Kotflix](https://github.com/PepeuFBV/KotFlix).

## Installation

Get the project from GitHub:

```bash
git clone https://github.com/PepeuFBV/Movie-Recommendation.git
```

## Project Structure and Files

The project contains 4 main files:

- `models.ipynb` - Jupyter Notebook containing the implementation of the recommendation algorithms.
- `fetch_data.py` - Python script to fetch data from TMDb API.

## Data files

final_data folder
- ratings.csv - Final ratings file, contains the userId, movieId and rating for each rating done by the users.
- movies_ids.csv - Contains information pertaining to the possible ids for the movies, has the movieId (MovieLens id), imdbId (IMDb id) and tmdbId (TMDb id).
- movies.csv - Contains information about the movies, such as the title, genres, release date, etc. But the only association with id is through the imdbId.


















