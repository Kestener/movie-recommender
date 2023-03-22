from flask import Flask
from flask import render_template, request
from simple_recommender import get_recommendations_random, get_recommendations_NMF
from utils import movies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Awesome Movie Recommender', movies=movies.title.to_list())

@app.route('/recommender')
def recommender():
    # a python dictionary consisting of
    # "name"-value pairs from the HTML form!

    if request.args.get('option') == 'Random':
        recs_ran = get_recommendations_random()
        return render_template('recommendations.html', movies = recs_ran)

    if request.args.get('option') == 'NMF':
        titles = request.args.getlist('title')
        ratings = request.args.getlist('rating')
        
        user_query = dict(zip(titles,ratings))
        for movie in user_query:
            user_query[movie] = float(user_query[movie])
        print(user_query)
        recs_nmf = get_recommendations_NMF(user_query)
        return render_template('recommendations.html', movies = recs_nmf)
    
    # at this point, we would then pass this
    #information as an argument into our recommender function.
    recs = get_recommendations_random()
    return render_template('recommendations.html', movies = recs)

if __name__ == "__main__":
    app.run(debug=True, port=5000)