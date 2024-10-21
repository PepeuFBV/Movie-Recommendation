# Movie-Recommendation

This repository focuses on developing a movie recommendation algorithm based on scores, aiming to suggest titles to users based on their previous ratings and liking's. The goal of this system is to identify which movies or series a user is likely to enjoy, assigning a score to each title based on their behavior and preferences.

By comparing the performance of these algorithms in the context of personalized recommendations, we can find the best model to increase user satisfaction on streaming platforms. The findings of this study could contribute to optimizing content delivery and production, as well as significantly improving the user experience in modern entertainment environments. Therefore, the development of an efficient recommendation engine is essential to elevate the level of user engagement.

Models such as Matrix Factorization algorithms (SVD, SVDpp, NMF), the Slope One algorithm and Co-Clustering, are used to predict the scores of movies and series. The data used in this study is the [MovieLens](https://grouplens.org/datasets/movielens/20m/) dataset, which contains information about user ratings and movie titles.

The repository also contains a script to fetch the remaining necessary data from The Movie Database (TMDb) API, such as movie genres, release dates, trailer links and other relevant information. The data is then preprocessed and saved in a CSV file to be used in the main application developed for using this project [Kotflix](https://github.com/PepeuFBV/KotFlix).

A paper was also written to explain the objectives and results of this project, which can be found [here](Leveraging_Machine_Learning_Algorithms_for_User_Centric_Movie_Recommendations.pdf).

## Installation

Get the project from GitHub:

```bash
git clone https://github.com/PepeuFBV/Movie-Recommendation.git
```

## Project Structure and Files

The project contains 5 main files:

- `models.ipynb` - Jupyter Notebook containing the implementation of the recommendation algorithms.
- `fetch_data.py` - Python script to fetch data from TMDb API.
- `analysis.ipynb` - Jupyter Notebook containing the analysis of the ratings' data.
- `dataset_treatment.ipynb` - Jupyter Notebook containing the treatment of the dataset.
- `send_data.py` - Python script to send the data to the Kotflix application (uses the `urls.txt` file).

## Data files

Create a data directory and download the MovieLens dataset and IMDb dataset. The MovieLens dataset can be downloaded from the [MovieLens](https://grouplens.org/datasets/movielens/20m/) website. The IMDb dataset can be downloaded from the [IMDb](https://www.imdb.com/interfaces/) website.

Then create a data directory and move the downloaded files to it, as well as make a subdirectory called final_data. The final data directory will contain the final dataset used in the project and ratings.csv, which is the dataset used in the analysis.

## Usage

Firstly run the `fetch_data.py` script to fetch the remaining data from TMDb API:

```bash
python fetch_data.py
```

Then run the `dataset_treatment.ipynb` notebook to preprocess the data and save it in a CSV file.

After that, run the `models.ipynb` notebook to train the recommendation models and evaluate their performance.

Furthermore, run the `analysis.ipynb` notebook to analyze the ratings' data.

Finally, run the `send_data.py` script to send the data to the Kotflix application:

```bash
python send_data.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
