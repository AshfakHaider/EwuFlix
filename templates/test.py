# print("Recommended Movie Indices:", recommended_movie_indices)


# Convert regression predictions to binary classification predictions
threshold = 0.5  # Adjust this threshold as needed
y_pred_binary = (y_pred >= threshold).astype(int)



# Print the recommended movie indices along with predicted and actual ratings
for i in range(5):  # Replace 10 with the number of recommendations you want
    movie_index = recommended_movie_indices[i]
    if movie_index < len(Y_test):
        predicted_rating = y_pred[movie_index]
        actual_rating = Y_test.iloc[movie_index]  # Use iloc to access the index in Y_test
        print(f"Movie Index: {movie_index}, Predicted Rating: {predicted_rating:.2f}, Actual Rating: {actual_rating:.2f}")
    else:
        print(f"Movie Index {movie_index} is not found in Y_test. Skipping this movie.")

# Calculate movie popularity based on user ratings (average rating)
movie_popularity = df.groupby('movie_id')['rating'].mean().reset_index()

# Sort movies by popularity (average rating) in descending order
top_popular_movies = movie_popularity.sort_values(by='rating', ascending=False)

# Recommend the top N popular movies
N = 10  # Change N to the number of recommendations you want
top_n_recommendations = top_popular_movies.head(N)

# Print the recommended movies with movie ID and average rating
print("Top", N, "Popular Movies:")
for index, row in top_n_recommendations.iterrows():
    movie_id = row['movie_id']
    average_rating = row['rating']
    print("Movie ID:", movie_id, "| Overall Rating:", average_rating)

import numpy as np

# Create a user-item matrix from the ratings data using pivot_table
user_item_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating', aggfunc='mean', fill_value=0)

# Print the available user IDs to select a valid target user
print("Available User IDs:", user_item_matrix.index)

# Specify a valid target user for whom you want to make recommendations
target_user_index = 123  # Replace '123' with the actual user ID you want to use

if target_user_index not in user_item_matrix.index:
    print(f"Invalid target user index: {target_user_index}. Please specify a valid user ID.")
else:
    # Continue with the collaborative filtering code
    similarities = []
    for user_index in range(user_item_matrix.shape[0]):
        if user_index == target_user_index:
            continue
        target_user = user_item_matrix.loc[target_user_index]
        other_user = user_item_matrix.iloc[user_index]
        dot_product = np.dot(target_user, other_user)
        norm_target_user = np.linalg.norm(target_user)
        norm_other_user = np.linalg.norm(other_user)
        similarity = dot_product / (norm_target_user * norm_other_user)
        similarities.append((user_index, similarity))

    # Sort users by similarity in descending order
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Choose the top N most similar users (e.g., N=2) and recommend items they liked
    N = 2
    recommended_items = set()
    for user_index, similarity in similarities[:N]:
        for item_index, rating in enumerate(user_item_matrix.iloc[user_index]):
            if rating > 0 and user_item_matrix.iloc[target_user_index, item_index] == 0:
                recommended_items.add(item_index)

    # Print the recommended item indices
    print("Recommended Item Indices:", recommended_items)




