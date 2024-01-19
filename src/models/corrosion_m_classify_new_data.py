import joblib
import pandas as pd
import os

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)

# Load the trained model
loaded_model = joblib.load('/Users/machinelearning/myfirstmlproject/machinelearning_projects/src/models/corrosion_detect_trained_model.pkl')

# Preprocess the new data (replace this with your actual preprocessing steps)
new_data = pd.DataFrame({
    'Temperature': [65.2, 72.5, 68.7],
    'Pressure': [1012.3, 1008.5, 1015.1],
    'Humidity': [40.1, 45.2, 39.8],
    'Weather_Condition': [1, 2, 3 ],
    'NDT_Result': [2, 1, 3]
})

# Encode categorical features in the new data (if needed)
# Ensure that the new data's format matches the training data

# Make predictions on the new data
predictions = loaded_model.predict(new_data)

# Interpret the predictions (map numeric labels to categories if necessary)
print(predictions)
