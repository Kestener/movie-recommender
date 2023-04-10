# Movie Recommender using NMF and Flask

This repository provides the code required to deploy a Non-Negative Matrix factorization model to generate movie recommendations based on user's input.
Deployed using Flask. 

## Structure of the repository

### 1. Installation

Simply clone the repository and pip install the libraries listed in the [requirements](requirements.txt) file.

### 2. Code

- [simple_recommender](simple_recommender.py) includes the functions called by the Streamlit application. References [utils](utils.py) for supporting functions.
- [app](app.py) is the Flask application, which requires the supporting folders [data](data/), [static](static/), and [templates](templates/).

### 3. Data
[data](data/) includes the list of [movies](data/movies.csv) and the [NMF_model](data/nmf_modelproj.pkl) used by the application.

### 4. Results
This repository demonstrates the use of recommender algorithms to generate movie recommendations based on user's preference.