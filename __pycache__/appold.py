from flask import Flask, request, render_template, redirect, url_for, session, flash, g
import mysql.connector
import secrets
from passlib.hash import bcrypt_sha256
import decimal
import pickle
import pandas as pd
import random
import numpy as np

# popular = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)


file_path = '/Users/syednawazishhaider/Documents/ewuflix/data_movies main.csv'
df = pd.read_csv(file_path)

model_file_path = 'model2.pkl'
model2 = pickle.load(open(model_file_path, 'rb'))

def load_dynamic_recommendation_model():
    # Generate a new random number between 3 and 10 each time the model is loaded
    random_number = random.randint(10, 20)

    # Load the model with the dynamic recommendations
    model_file_path = 'model.pkl'
    model = pickle.load(open(model_file_path, 'rb'))

    # Return the model and the dynamic random number
    return model, random_number



# def recommend_movies_for_user(user_id, df, num_recommendations=10):
#     # Filter the dataset to get the user's rated movies and ratings
#     user_ratings = df[df['user_id'] == user_id][['movie_id', 'user_id', 'rating1', 'rating2', 'rating3', 'rating4']]

#     # Calculate the average rating for each movie
#     average_ratings = user_ratings[['rating1', 'rating2', 'rating3', 'rating4']].mean(axis=0)

#     # Calculate similarity scores with other movies
#     similarity_scores = df[['movie_id', 'user_id', 'rating1', 'rating2', 'rating3', 'rating4']].apply(
#         lambda row: np.dot(average_ratings, row[['rating1', 'rating2', 'rating3', 'rating4']]), axis=1)

#     # Sort movies by similarity score in descending order
#     similar_movies = df.copy()
#     similar_movies['similarity_score'] = similarity_scores
#     similar_movies = similar_movies.sort_values(by='similarity_score', ascending=False)

#     # Filter out movies already rated by the user
#     rated_movie_ids = user_ratings['movie_id'].tolist()
#     similar_movies = similar_movies[~similar_movies['movie_id'].isin(rated_movie_ids)]

#     # Get the top N recommended movies
#     recommended_movies = similar_movies.head(num_recommendations)

#     return recommended_movies
# def recommend_movies_for_user():

    
#     num_recommendations=10
#     df
#     file_path = 'model2.pkl'
#     newModel = pickle.load(open(file_path, 'rb'))
#     user_id = random.randint(1, 6078)
#     # Filter the dataset to get the user's rated movies and ratings
#     user_ratings = df[df['user_id'] == user_id][['movie_id', 'user_id', 'rating1', 'rating2', 'rating3', 'rating4']]

#     # Calculate the average rating for each movie
#     average_ratings = user_ratings[['rating1', 'rating2', 'rating3', 'rating4']].mean(axis=0)

#     # Calculate similarity scores with other movies
#     similarity_scores = df[['movie_id', 'user_id', 'rating1', 'rating2', 'rating3', 'rating4']].apply(
#         lambda row: np.dot(average_ratings, row[['rating1', 'rating2', 'rating3', 'rating4']]), axis=1)

#     # Sort movies by similarity score in descending order
#     similar_movies = df.copy()
#     similar_movies['similarity_score'] = similarity_scores
#     similar_movies = similar_movies.sort_values(by='similarity_score', ascending=False)

#     # Filter out movies already rated by the user
#     rated_movie_ids = user_ratings['movie_id'].tolist()
#     similar_movies = similar_movies[~similar_movies['movie_id'].isin(rated_movie_ids)]

#     # Get the top N recommended movies
#     recommended_movies = similar_movies.head(num_recommendations)

#     return recommended_movies, user_id , newModel

def recommend_movies_for_user():

    file_path = 'model2.pkl'
    newModel = pickle.load(open(file_path, 'rb'))
    num_recommendations = 10
    user_id = random.randint(1, 6078)

    # Calculate movie recommendations based on the dynamic user ID
    user_ratings = df[df['user_id'] == user_id][['movie_id', 'user_id', 'rating1', 'rating2', 'rating3', 'rating4']]
    # You can customize the logic below based on your specific recommendation strategy

    # Calculate the average rating for each movie
    average_ratings = user_ratings[['rating1', 'rating2', 'rating3', 'rating4']].mean(axis=0)

    # Calculate similarity scores with other movies
    similarity_scores = df[['movie_id', 'user_id', 'rating1', 'rating2', 'rating3', 'rating4']].apply(
        lambda row: np.dot(average_ratings, row[['rating1', 'rating2', 'rating3', 'rating4']]), axis=1)

    # Sort movies by similarity score in descending order
    similar_movies = df.copy()
    similar_movies['similarity_score'] = similarity_scores
    similar_movies = similar_movies.sort_values(by='similarity_score', ascending=False)

    # Filter out movies already rated by the user
    rated_movie_ids = user_ratings['movie_id'].tolist()
    similar_movies = similar_movies[~similar_movies['movie_id'].isin(rated_movie_ids)]

    # Get the top N recommended movies
    recommended_movies = similar_movies.head(num_recommendations)

    return recommended_movies, user_id,newModel



# Configure the MySQL database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ewuflix2'

# Secret key for session management
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

# Define the database connection function
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
    return g.db

@app.route('/recommendations')
def get_recommendations():
    # Load the model and get the dynamic random number
    recommendation_model, random_number = load_dynamic_recommendation_model()

    # Calculate movie popularity based on user ratings (average rating)
    movie_popularity = df.groupby('movie_id')['rating'].mean().reset_index()

    # Sort movies by popularity (average rating) in descending order
    top_popular_movies = movie_popularity.sort_values(by='rating', ascending=False)

    N = random_number   # Use the generated random number as the number of recommendations

    # Select the top N popular movies as recommendations
    top_n_recommendations = top_popular_movies.head(N)

    # You can then pass top_n_recommendations or its relevant data to your template

    # Return recommendations as a response
    return render_template('recommendations.html', movieId=list(top_n_recommendations['movie_id']),overallRating=list(top_n_recommendations['rating']))


@app.route('/recommend_movies')
def recommend_movies():

    recommended_movies, user_id, newModel  = recommend_movies_for_user()
    return render_template('recommend_movies.html', user_id=user_id, movieId=list(newModel['movie_id']))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = get_db().cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # Extract the stored hashed password from the database
            stored_hashed_password = user[3]

            if bcrypt_sha256.verify(password, stored_hashed_password):
                session['user'] = {'id': user[0], 'username': user[1]}
                flash('Login successful!', 'success')
                return redirect(url_for('movies'))

        flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')


@app.route('/')
def home():
    if 'user' in session:
        username = session['user']['username']
        return f'Welcome to {username}'
    else:
        flash('You must be logged in to access this page.', 'danger')
        return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Hash the password using Passlib
        hashed_password = bcrypt_sha256.hash(password)

        cursor = get_db().cursor()
        cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', (username, hashed_password, email))
        get_db().commit()
        cursor.close()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/upload_movie', methods=['GET', 'POST'])
def upload_movie():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.files['image']

        # Save the image to the 'static/images' folder
        image.save('static/images/' + image.filename)
        cursor = get_db().cursor()
        cursor.execute('INSERT INTO movies (title, description, image_path) VALUES (%s, %s, %s)', (title, description, 'static/images/' + image.filename))
        get_db().commit()
        cursor.close()

    return render_template('upload_movie.html')


@app.route('/movies')
def movies():
    cursor = get_db().cursor()
    cursor.execute('SELECT id, title, description, image_path FROM movies')
    movies = cursor.fetchall()
    cursor.close()

    username = None
    if 'user' in session:
        username = session['user']['username']

    return render_template('movies.html', movies=movies, username=username)



# @app.route('/movie/<int:movie_id>')
# def movie_details(movie_id):
#     cursor = get_db().cursor()
#     cursor.execute('SELECT id, title, description, image_path FROM movies WHERE id = %s', (movie_id,))
#     movie = cursor.fetchone()

        
#     # Calculate the average rating and count the number of ratings for the movie
#     cursor.execute('SELECT COUNT(*) FROM movie_ratings WHERE movie_id = %s', (movie_id,))
#     num_ratings = cursor.fetchone()[0]  # Get the count of ratings
    
#     if num_ratings > 0:
#         cursor.execute('SELECT AVG(overall_rating) FROM movie_ratings WHERE movie_id = %s', (movie_id,))
#         average_rating = cursor.fetchone()[0]  # Get the average rating
    
#         # Sum all the values in the overall_rating column for the specific movie
#         cursor.execute('SELECT SUM(overall_rating) FROM movie_ratings WHERE movie_id = %s', (movie_id,))
#         total_rating_sum = cursor.fetchone()[0]  # Get the sum of overall ratings
        
#         # Calculate the average rating by dividing the total rating sum by the number of ratings
#         calculated_average_rating = total_rating_sum / num_ratings
    
#     cursor.close()



#     username = session.get('user', {}).get('username')

#     #return render_template('movie_details.html', movie=movie, username=username)
#     return render_template('movie_details.html', movie=movie, username=username, average_rating=average_rating, num_ratings=num_ratings, total_rating_sum=total_rating_sum, calculated_average_rating=calculated_average_rating)
@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    cursor = get_db().cursor()
    cursor.execute('SELECT id, title, description, image_path FROM movies WHERE id = %s', (movie_id,))
    movie = cursor.fetchone()
    
    # Initialize the variables to default values
    average_rating = None
    num_ratings = 0
    total_rating_sum = 0
    calculated_average_rating = None

    # Check if there are ratings available for the movie
    cursor.execute('SELECT COUNT(*) FROM movie_ratings WHERE movie_id = %s', (movie_id,))
    num_ratings = cursor.fetchone()[0]  # Get the count of ratings

    if num_ratings > 0:
        cursor.execute('SELECT AVG(overall_rating) FROM movie_ratings WHERE movie_id = %s', (movie_id,))
        average_rating = cursor.fetchone()[0]  # Get the average rating

        # Sum all the values in the overall_rating column for the specific movie
        cursor.execute('SELECT SUM(overall_rating) FROM movie_ratings WHERE movie_id = %s', (movie_id,))
        total_rating_sum = cursor.fetchone()[0]  # Get the sum of overall ratings

        # Calculate the average rating by dividing the total rating sum by the number of ratings
        calculated_average_rating = total_rating_sum / num_ratings

    cursor.close()

    username = session.get('user', {}).get('username')

    return render_template('movie_details.html', movie=movie, username=username, average_rating=average_rating, num_ratings=num_ratings, total_rating_sum=total_rating_sum, calculated_average_rating=calculated_average_rating)




@app.route('/rate_movie/<int:movie_id>', methods=['POST'])
def rate_movie(movie_id):
    if 'user' not in session:
        flash('You must be logged in to rate movies.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user']['id']
    rating1 = int(request.form['rating1'])
    rating2 = int(request.form['rating2'])
    rating3 = int(request.form['rating3'])
    rating4 = int(request.form['rating4'])

    # Calculate the overall rating (average of the four ratings)
    overall_rating = (rating1 + rating2 + rating3 + rating4) / 4.0

    cursor = get_db().cursor()
    cursor.execute('INSERT INTO movie_ratings (user_id, movie_id, rating1, rating2, rating3, rating4, overall_rating) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                   (user_id, movie_id, rating1, rating2, rating3, rating4, overall_rating))
    get_db().commit()
    cursor.close()

    flash('Rating submitted successfully!', 'success')
    return redirect(url_for('movie_details', movie_id=movie_id))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
