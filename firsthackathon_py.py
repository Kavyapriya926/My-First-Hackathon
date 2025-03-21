# -*- coding: utf-8 -*-
"""Firsthackathon.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/116qt27A0uS-mRtyJAQJU1pBCKUL8UEWS
"""

from google.colab import files
uploaded=files.upload()

from google.colab import drive
# Step 1: Mount Google Drive to access files stored in it
drive.mount('/content/drive')

# Step 2: Choose to either upload a file from your local machine or access a file from Google Drive

# Option 1: Access a file from Google Drive
google_drive_file_path = '/content/drive/My Drive/train -train.csv.csv'
df_drive = pd.read_csv(google_drive_file_path)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('train - train.csv.csv')

# Calculate promotion rate by department
promotion_rate = data.groupby('department')['is_promoted'].mean() * 100

# Plotting the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=promotion_rate.index, y=promotion_rate.values, palette='viridis')
plt.title('Promotion Rate by Department')
plt.xlabel('Department')
plt.ylabel('Promotion Rate (%)')
plt.xticks(rotation=45)
plt.show()

# Calculate promotion rate by education level
promotion_rate_edu = data.groupby('education')['is_promoted'].mean() * 100

# Plotting the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=promotion_rate_edu.index, y=promotion_rate_edu.values, palette='coolwarm')
plt.title('Promotion Rate by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Promotion Rate (%)')
plt.xticks(rotation=45)
plt.show()

# Calculate promotion rate by gender
promotion_rate_gender = data.groupby('gender')['is_promoted'].mean() * 100

# Plotting the bar chart
plt.figure(figsize=(6, 6))
sns.barplot(x=promotion_rate_gender.index, y=promotion_rate_gender.values, palette='magma')
plt.title('Promotion Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Promotion Rate (%)')
plt.show()

# Calculate promotion rate by recruitment channel
promotion_rate_recruitment = data.groupby('recruitment_channel')['is_promoted'].mean() * 100

# Plotting the bar chart
plt.figure(figsize=(8, 6))
sns.barplot(x=promotion_rate_recruitment.index, y=promotion_rate_recruitment.values, palette='plasma')
plt.title('Promotion Rate by Recruitment Channel')
plt.xlabel('Recruitment Channel')
plt.ylabel('Promotion Rate (%)')
plt.xticks(rotation=45)
plt.show()

# Plotting the box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='is_promoted', y='avg_training_score', data=data, palette='Set2')
plt.title('Average Training Score for Promoted vs Non-Promoted Employees')
plt.xlabel('Promotion Status (0: Not Promoted, 1: Promoted)')
plt.ylabel('Average Training Score')
plt.show()

# Plotting the box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='is_promoted', y='length_of_service', data=data, palette='Set3')
plt.title('Length of Service for Promoted vs Non-Promoted Employees')
plt.xlabel('Promotion Status (0: Not Promoted, 1: Promoted)')
plt.ylabel('Length of Service (Years)')
plt.show()

# Calculate average previous year's rating by promotion status
avg_rating = data.groupby('is_promoted')['previous_year_rating'].mean()

# Plotting the bar chart
plt.figure(figsize=(6, 6))
sns.barplot(x=avg_rating.index, y=avg_rating.values, palette='coolwarm')
plt.title('Average Previous Year Rating for Promoted vs Non-Promoted Employees')
plt.xlabel('Promotion Status (0: Not Promoted, 1: Promoted)')
plt.ylabel('Average Previous Year Rating')
plt.show()

# Plotting the histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='age', hue='is_promoted', kde=True, palette='Set1', bins=20)
plt.title('Age Distribution for Promoted vs Non-Promoted Employees')
plt.xlabel('Age')
plt.ylabel('Number of Employees')
plt.legend(title='Promotion Status', labels=['Not Promoted', 'Promoted'])
plt.show()

# Calculate percentage of employees who won awards by promotion status
awards_won = data.groupby('is_promoted')['awards_won?'].mean() * 100

# Plotting the bar chart
plt.figure(figsize=(6, 6))
sns.barplot(x=awards_won.index, y=awards_won.values, palette='viridis')
plt.title('Percentage of Employees Who Won Awards by Promotion Status')
plt.xlabel('Promotion Status (0: Not Promoted, 1: Promoted)')
plt.ylabel('Percentage of Employees Who Won Awards')
plt.show()

!pip install pandas scikit-learn matplotlib seaborn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('train - train.csv.csv')

# Display the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Handle missing values (if any)
# For example, fill missing 'previous_year_rating' with the median
data['previous_year_rating'].fillna(data['previous_year_rating'].median(), inplace=True)

# Drop rows with missing values in other columns (if necessary)
data.dropna(inplace=True)

# Convert categorical variables into numerical using one-hot encoding
data = pd.get_dummies(data, columns=['department', 'region', 'education', 'gender', 'recruitment_channel'], drop_first=True)

# Separate features (X) and target (y)
X = data.drop('is_promoted', axis=1)
y = data['is_promoted']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the datasets
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Initialize the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Get feature importances
importances = rf_model.feature_importances_

# Create a DataFrame for visualization
feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
})

# Sort by importance
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Plot feature importance
plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette='viridis')
plt.title('Feature Importance for Predicting Employee Promotions')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()

import joblib

# Save the model
joblib.dump(rf_model, 'random_forest_promotion_model.pkl')

# Load the model (if needed)
# loaded_model = joblib.load('random_forest_promotion_model.pkl')

# Example: Load new data
new_data = pd.read_csv('train - train.csv.csv')  # Replace with your new data file

# Preprocess the new data (same steps as above)
new_data = pd.get_dummies(new_data, columns=['department', 'region', 'education', 'gender', 'recruitment_channel'], drop_first=True)

# Ensure the columns match the training data
new_data = new_data.reindex(columns=X.columns, fill_value=0)

# Make predictions
new_predictions = rf_model.predict(new_data)

# Add predictions to the new data
new_data['is_promoted'] = new_predictions

# Display the results
print(new_data[['employee_id', 'is_promoted']])

from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Calculate key metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print the metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)

# Generate a detailed classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Generate and plot the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Not Promoted', 'Promoted'],
            yticklabels=['Not Promoted', 'Promoted'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

