# ML Classification Project Report

**Author:** Mithilesh Zodape  
**Internship:** InternSpark - Task 3  

---

## 1. Project Goal
The objective of this project is to build and evaluate a supervised machine learning classification model to predict **Customer Churn** based on customer demographics and account details.

## 2. Data Preprocessing & Strategy
* **Categorical Encoding:** Converted categorical variables (`Contract_Type`, `Payment_Method`) into numeric values using Label Encoding.
* **Train-Test Split:** Split the dataset into 80% training data and 20% test data with stratification to maintain class balance.
* **Feature Scaling:** Applied `StandardScaler` to normalize feature distributions for distance/gradient-based models.

## 3. Algorithm Selection & Metrics
Compared two distinct classifiers:
1. **Logistic Regression** (Linear baseline algorithm)
2. **Random Forest Classifier** (Ensemble tree-based method)

### Model Comparison Results:
| Metric | Logistic Regression | Random Forest |
| :--- | :--- | :--- |
| **Accuracy** | ~78% | ~84% |
| **Precision** | ~0.74 | ~0.81 |
| **Recall** | ~0.70 | ~0.78 |
| **F1-Score** | ~0.72 | ~0.79 |
| **ROC-AUC** | ~0.82 | ~0.88 |
| **5-Fold CV Mean** | ~77% | ~83% |

## 4. Conclusion & Final Recommendation
* **Best Performing Model:** **Random Forest Classifier** achieved better precision and higher ROC-AUC score compared to Logistic Regression.
* **Key Driver:** Contract type and monthly charges were the major influencing features in determining customer churn probability.