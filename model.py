import pandas as pd
import numpy as np
import random
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



#file_path = '/Users/syednawazishhaider/Documents/ewuflix/data_movies main.csv'
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


# Calculate movie popularity based on user ratings (average rating)
movie_popularity = df.groupby('movie_id')['rating'].mean().reset_index()

# Sort movies by popularity (average rating) in descending order
top_popular_movies = movie_popularity.sort_values(by='rating', ascending=False)

random_number = random.randint(3, 10)

N = random_number   # Change N to the number of recommendations you want
top_n_recommendations = top_popular_movies.head(N)

# Print the recommended movies with movie ID and average rating
print("Top", N, "Popular Movies:")
for index, row in top_n_recommendations.iterrows():
    movie_id = row['movie_id']
    average_rating = row['rating']
    print("Movie ID:", movie_id, "| Overall Rating:", average_rating)

pickle.dump(top_n_recommendations, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))