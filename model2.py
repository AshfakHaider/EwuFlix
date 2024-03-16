import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, median_absolute_error, mean_squared_log_error, r2_score
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, accuracy_score
import pickle
import random



file_path = '/Users/syednawazishhaider/Documents/ewuflix/dataset final.csv'
df = pd.read_csv(file_path)

min_values = df[['rating1', 'rating2', 'rating3', 'rating4']].min()
max_values = df[['rating1', 'rating2', 'rating3', 'rating4']].max()
df[['rating1', 'rating2', 'rating3', 'rating4']] = (df[['rating1', 'rating2', 'rating3', 'rating4']] - min_values) / (max_values - min_values)


features = ['user_id', 'rating1', 'rating2', 'rating3', 'rating4', 'movie_id']
X = df[features]
Y = df['rating']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

def fitness_function(features, X_train, Y_train):

    selected_features = X_train.iloc[:, features].values
    y = Y_train.values
    predicted_ratings = np.mean(selected_features, axis=1)
    mse = mean_squared_error(y, predicted_ratings)
    return mse

num_particles = X_train.shape[0]
num_features = X_train.shape[1]
max_iterations = 5
def pso_algorithm(X_train, Y_train):
    swarm = np.random.randint(0, 2, size=(num_particles, num_features))
    best_positions = swarm.copy()
    best_fitness = np.inf * np.ones(num_particles)
    global_best_position = None
    global_best_fitness = np.inf

    for iteration in range(max_iterations):
        fitness_values = np.array([fitness_function(features, X_train, Y_train) for features in swarm])


        mask = fitness_values < best_fitness
        best_positions[mask] = swarm[mask]
        best_fitness[mask] = fitness_values[mask]

        best_particle_index = np.argmin(best_fitness)
        if best_fitness[best_particle_index] < global_best_fitness:
            global_best_position = best_positions[best_particle_index].copy()
            global_best_fitness = best_fitness[best_particle_index]


        w = 0.5
        c1 = 1.5
        c2 = 2.0
        r1 = np.random.rand(num_particles, num_features)
        r2 = np.random.rand(num_particles, num_features)
        velocity = w * swarm + c1 * r1 * (best_positions - swarm) + c2 * r2 * (global_best_position - swarm)
        velocity = np.clip(velocity, 0, 1)
        swarm = np.where(velocity < 0.5, 0, 1)

    return global_best_position, global_best_fitness

best_features, best_fitness = pso_algorithm(X_train, Y_train)

selected_features = X_train.iloc[:, best_features]

scaler = StandardScaler()
selected_features = scaler.fit_transform(selected_features)


pca = PCA(n_components=0.95)
selected_features = pca.fit_transform(selected_features)

user_item_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating', aggfunc='mean', fill_value=0)

user_item_matrix = user_item_matrix.astype(np.float32)
n_components = 5
svd = TruncatedSVD(n_components=n_components)
user_feature_matrix = svd.fit_transform(user_item_matrix)
dbscan = DBSCAN(eps=0.5, min_samples=2)
labels = dbscan.fit_predict(user_feature_matrix)

cluster_similarity = cosine_similarity(user_feature_matrix)

for i in range(len(labels)):
    if labels[i] != -1:
        similar_clusters = np.where(cluster_similarity[i] > 0.5)[0]
        if len(similar_clusters) > 1:
            for j in similar_clusters:
                labels[labels == labels[j]] = labels[i]

unique_labels, label_counts = np.unique(labels, return_counts=True)
label_mapping = {}
new_label = 1
for label, count in zip(unique_labels, label_counts):
    if count > 0:
        label_mapping[label] = new_label
        new_label += 1

reassigned_labels = np.array([label_mapping[label] for label in labels])

for i in range(len(reassigned_labels)):
    cluster_label = reassigned_labels[i]
    nearest_neighbor_index = cluster_similarity[i].argmax()
    nearest_neighbor_distance = cluster_similarity[i].max()

    if cluster_label == -1:
        cluster_type = "Noise"
    else:
        cluster_type = "Core"

    print(f"Point: {i} | Distance to Nearest Neighbor: {nearest_neighbor_distance} | Cluster Label: {cluster_type}")



nearest_neighbor_distances = np.array([cluster_similarity[i].max() for i in range(len(labels))])



scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

ann_model = MLPRegressor(hidden_layer_sizes=(100, 50), activation='relu', random_state=0)

ann_model.fit(X_train_scaled, Y_train)

X_test_scaled = scaler.transform(X_test)
y_pred = ann_model.predict(X_test_scaled)

recommended_movie_id = y_pred.argsort()[:10]

def recommend_movies_for_user():
    user_id = random.randint(1, 6078)
    num_recommendations=10
    # Filter the dataset to get the user's rated movies and ratings
    user_ratings = df[df['user_id'] == user_id][['movie_id', 'user_id', 'rating1', 'rating2', 'rating3', 'rating4']]

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

    return recommended_movies

recommended_movies = recommend_movies_for_user()


# Print the recommended movies
for index, row in recommended_movies.iterrows():
    print(f"Movie ID: {int(row['movie_id'])}, Similarity Score: {row['similarity_score']}")



pickle.dump(recommended_movies, open('model2.pkl','wb'))

 #Loading model to compare the results
model2 = pickle.load(open('model.pkl','rb'))
