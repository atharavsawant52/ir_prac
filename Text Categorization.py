from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

# Sample dataset
text = [
"I have fever",
"high fever and cough",
"running nose and cold",
"flu symptoms",
"covid positive fever",
"cold and headache"
]

labels = ["flu","flu","flu","flu","covid","flu"]

# Train test split
X_train,X_test,y_train,y_test = train_test_split(text,labels,test_size=0.3)

# Convert text to numbers
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_counts,y_train)

# Prediction
pred = model.predict(X_test_counts)

print("Accuracy:",accuracy_score(y_test,pred))
print("\nClassification Report:\n")
print(classification_report(y_test,pred))

print("performed by 44_Atharav Sawant")