# Task 3: Machine Learning Classification Project
# Topic: Customer Churn Prediction
# Student Name: Mithilesh Zodape

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, roc_curve
)

# -------------------------------------------------------------
# 1. Dataset Generation (Synthetic Customer Churn Dataset)
# -------------------------------------------------------------
np.random.seed(42)
n_samples = 600

data = {
    'Age': np.random.randint(18, 65, size=n_samples),
    'Tenure_Months': np.random.randint(1, 60, size=n_samples),
    'Monthly_Charges': np.random.uniform(20.0, 120.0, size=n_samples),
    'Contract_Type': np.random.choice(['Month-to-month', 'One year', 'Two year'], size=n_samples),
    'Payment_Method': np.random.choice(['Electronic Check', 'Mailed Check', 'Credit Card'], size=n_samples)
}

df = pd.DataFrame(data)

# Logic for Churn probabilities
churn_prob = (
    0.3 * (df['Contract_Type'] == 'Month-to-month') +
    0.2 * (df['Monthly_Charges'] > 75) -
    0.15 * (df['Tenure_Months'] > 24)
)
churn_prob = np.clip(churn_prob + np.random.normal(0, 0.1, n_samples), 0, 1)
df['Churn'] = (churn_prob > 0.35).astype(int)

print("--- Initial Data Snapshot ---")
print(df.head())
print("\nDataset Info:")
print(df.info())

# -------------------------------------------------------------
# 2. Data Preprocessing & Encoding
# -------------------------------------------------------------
le = LabelEncoder()
df['Contract_Type'] = le.fit_transform(df['Contract_Type'])
df['Payment_Method'] = le.fit_transform(df['Payment_Method'])

X = df.drop('Churn', axis=1)
y = df['Churn']

# Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -------------------------------------------------------------
# 3. Model Training & Comparison
# -------------------------------------------------------------
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    # Use scaled data for Logistic Regression, raw data works fine for Trees
    X_tr = X_train_scaled if name == 'Logistic Regression' else X_train
    X_te = X_test_scaled if name == 'Logistic Regression' else X_test
    
    # Train
    model.fit(X_tr, y_train)
    
    # Predictions
    y_pred = model.predict(X_te)
    y_proba = model.predict_proba(X_te)[:, 1]
    
    # Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    
    # Cross-validation score (5 fold)
    cv_scores = cross_val_score(model, X_tr, y_train, cv=5, scoring='accuracy')
    
    results[name] = {
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1-Score': f1,
        'ROC-AUC': auc,
        'CV_Mean_Acc': cv_scores.mean(),
        'y_proba': y_proba,
        'y_pred': y_pred
    }

# Display Metrics Table
metrics_df = pd.DataFrame(results).T.drop(['y_proba', 'y_pred'], axis=1)
print("\n--- Model Comparison Summary ---")
print(metrics_df)

# -------------------------------------------------------------
# 4. Visualizations & Plots
# -------------------------------------------------------------
plt.figure(figsize=(12, 5))

# Plot 1: Confusion Matrix for Random Forest
plt.subplot(1, 2, 1)
cm = confusion_matrix(y_test, results['Random Forest']['y_pred'])
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Random Forest - Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# Plot 2: ROC Curves comparison
plt.subplot(1, 2, 2)
for name in models.keys():
    fpr, tpr, _ = roc_curve(y_test, results[name]['y_proba'])
    plt.plot(fpr, tpr, label=f"{name} (AUC = {results[name]['ROC-AUC']:.2f})")

plt.plot([0, 1], [0, 1], 'k--', label='Random Guess')
plt.title('ROC-AUC Curves')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()

plt.tight_layout()
plt.savefig('classification_results.png')
print("\nPlot saved successfully as 'classification_results.png'")