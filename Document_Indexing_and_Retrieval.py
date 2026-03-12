import nltk
from nltk.corpus import stopwords

# download stopwords
nltk.download('stopwords')

doc1 = "The quick brown fox jumped over the lazy dog"
doc2 = "The lazy dog slept in the sun"

stop = set(stopwords.words('english'))

t1 = doc1.lower().split()
t2 = doc2.lower().split()

terms = set(t1+t2)

for term in terms:
    if term in stop:
        continue
    
    out = ""
    if term in t1:
        out += f"Document 1({t1.count(term)}), "
    if term in t2:
        out += f"Document 2({t2.count(term)}), "
        
    print(term,"->",out)

