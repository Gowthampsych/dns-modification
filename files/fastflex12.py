import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from tqdm import tqdm  # Import tqdm for progress tracking
import re
import joblib

# Load datasets
train_data = pd.read_csv("Webpages_Classification_train_data.csv")
test_data = pd.read_csv("Webpages_Classification_test_data.csv")

# Data Preprocessing
train_data.dropna(inplace=True)  # Drop rows with missing values
test_data.dropna(inplace=True)


# Feature Engineering
# Considering only IP addresses for classification
X_train = train_data['ip_add']
y_train = train_data['label']
X_test = test_data['ip_add']
y_test = test_data['label']

# Model Selection and Training
# You can use any other algorithm as well, like SVM, Logistic Regression, etc.
vectorizer = TfidfVectorizer(sublinear_tf=True, encoding='utf-8', decode_error='ignore', stop_words='english')
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Training with progress tracking
with tqdm(total=len(X_train), desc="Training") as pbar:
    rf_classifier.fit(X_train_vectorized, y_train)
    pbar.update(len(X_train))

# Evaluation
predictions = rf_classifier.predict(X_test_vectorized)
print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))

# Serialize the trained model and vectorizer
joblib.dump(rf_classifier, 'rf_classifier_model.joblib')
joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')

# Prediction
# Handling case when there are no FastFlex IPs
if len(fastflex_ips) > 0:
    fastflex_predictions = rf_classifier.predict(vectorizer.transform(list(fastflex_ips)))
else:
    fastflex_predictions = []

# Export Results
fastflex_df = pd.DataFrame(list(fastflex_ips), columns=['FastFlex_IP'])
fastflex_df['Prediction'] = fastflex_predictions
fastflex_df.to_csv("FastFlex_IPs_Predictions.csv", index=False)
