# SmartAI Categorizer – GHCI 25 Hackathon Submission

## Overview
SmartAI Categorizer is a standalone AI system designed to classify raw financial transaction strings (e.g., “Starbucks”) into meaningful categories (e.g., “Dining”) without relying on external APIs. Built for the GHCI 25 AI Hackathon, this solution emphasizes autonomy, explainability, and responsible AI practices.

## Features
- ✅ Logistic Regression model with TF-IDF vectorization
- ✅ Configurable taxonomy via `categories.json`
- ✅ SHAP-based explainability for classification decisions
- ✅ CLI feedback loop for user corrections
- ✅ Macro F1-score ≥ 0.90 on synthetic dataset
- ✅ Bias mitigation and robust handling of noisy inputs

## How to Run

### 1. Install Dependencies
```bash
pip install pandas scikit-learn shap joblib
