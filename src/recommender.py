import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Veri setini yükle
movies = pd.read_csv("data/movies.csv")

# Eksik açıklamaları doldur
movies['overview'] = movies['overview'].fillna('')

# TF-IDF vektörizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# Kosinüs benzerliği
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Film isimlerini index ile eşle
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def recommend(title, num_recommendations=5):
    """Verilen film adına göre benzer filmleri önerir."""
    if title not in indices:
        return [f"Film bulunamadı: {title}"]
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    film = "The Dark Knight"
    print(f"{film} için öneriler:")
    for m in recommend(film):
        print(" -", m)
