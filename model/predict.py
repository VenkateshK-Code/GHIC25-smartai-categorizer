import joblib
import sys

model = joblib.load('model/model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

transaction = sys.argv[1]
X_vec = vectorizer.transform([transaction])
pred = model.predict(X_vec)[0]
conf = model.predict_proba(X_vec).max()

print(f"Prediction: {pred} | Confidence: {conf:.2f}")
