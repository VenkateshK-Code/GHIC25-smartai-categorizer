import joblib
import shap
import pandas as pd

model = joblib.load('model/model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

explainer = shap.Explainer(model, vectorizer.transform)
sample = ["Starbucks"]
X_sample = vectorizer.transform(sample)

shap_values = explainer(X_sample)
shap.plots.text(shap_values[0])
