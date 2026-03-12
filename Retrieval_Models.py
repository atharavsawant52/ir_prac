#Boolean Retrieval Model
docs = {
1:"apple banana orange",
2:"apple banana",
3:"banana orange",
4:"apple"
}

index = {}

for id,text in docs.items():
    for w in text.split():
        index.setdefault(w,set()).add(id)

# Queries
q1 = index["apple"] & index["banana"]
q2 = index["apple"] | index["orange"]
q3 = set(docs.keys()) - index["orange"]

print("apple AND banana :",sorted(q1))
print("apple OR orange :",sorted(q2))
print("NOT orange :",sorted(q3))


#TF-IDF + Cosine Similarity

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright"
]

query = ["The sky"]

tf = TfidfVectorizer()

doc_vec = tf.fit_transform(docs)
query_vec = tf.transform(query)

sim = cosine_similarity(query_vec, doc_vec)

for i in range(len(docs)):
    print("TF-IDF for document",i+1,":",doc_vec[i].toarray()[0])

print("\nCosine Similarity:",sim)
