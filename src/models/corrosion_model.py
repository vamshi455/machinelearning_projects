import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib


# Load the data into a DataFrame
data = pd.read_csv('/Users/machinelearning/myfirstmlproject/machinelearning_projects/data/raw/corrosion_detection_data/oil_gas_corrosion_data.csv')

# Define the features and target variable
features = ['Temperature', 'Pressure', 'Humidity', 'Weather_Condition', 'NDT_Result']
target = 'Corrosion_Level'

# Prepare the data for modeling
X = data[features]
y = data[target]

# Encode categorical features (Weather_Condition and NDT_Result)
label_encoder = LabelEncoder()
X['Weather_Condition'] = label_encoder.fit_transform(X['Weather_Condition'])
X['NDT_Result'] = label_encoder.fit_transform(X['NDT_Result'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

classification_rep = classification_report(y_test, y_pred)
print('Classification Report:\n', classification_rep)

# Save the trained model to a .pkl file
model_filename = '/Users/machinelearning/myfirstmlproject/machinelearning_projects/src/models/corrosion_detect_trained_model.pkl'
joblib.dump(clf, model_filename)
