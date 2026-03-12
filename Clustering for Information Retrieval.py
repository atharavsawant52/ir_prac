from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

docs = [
"Cats are agile animals",
"Dogs are loyal pets",
"Sun rises in the east",
"Many cats climb trees"
]

# Convert text to TF-IDF vectors
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

# Print cluster for each document
for i, label in enumerate(kmeans.labels_):
    print("Document", i, "Cluster:", label)

print("performed by 44_Atharav Sawant")