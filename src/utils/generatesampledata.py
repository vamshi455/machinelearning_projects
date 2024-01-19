import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Define equipment master data
equipment_master = pd.DataFrame({
    'Equipment_ID': ['EQ001', 'EQ002', 'EQ003', 'EQ004', 'EQ005', 'EQ006', 'EQ007', 'EQ008', 'EQ009', 'EQ010'],
    'Material_Type': ['Carbon Steel', 'Stainless Steel', 'Aluminum', 'Carbon Steel', 'Stainless Steel', 'Carbon Steel', 'Stainless Steel', 'Aluminum', 'Carbon Steel', 'Stainless Steel'],
    'Coating_Type': ['Paint', 'Coated', 'Uncoated', 'Paint', 'Coated', 'Uncoated', 'Paint', 'Uncoated', 'Coated', 'Coated'],
    'Equipment_Age': [5, 10, 8, 12, 15, 7, 9, 6, 11, 13],
})

# Generate sample data for 100,000 records
timestamps = [datetime(2023, 1, 1, 8, 0, 0) + timedelta(seconds=i) for i in range(100000)]
equipment_ids = random.choices(equipment_master['Equipment_ID'], k=100000)
corrosion_levels = random.choices(['Normal', 'Mild', 'Severe'], k=100000)
temperatures = np.random.uniform(60, 75, 100000)
pressures = np.random.uniform(990, 1030, 100000)
humidity = np.random.uniform(40, 55, 100000)
weather_conditions = random.choices(['Sunny', 'Partly Cloudy', 'Rainy', 'Cloudy'], k=100000)
ndt_results = random.choices(['Pass', 'Fail'], k=100000)

# Create the DataFrame
data = pd.DataFrame({
    'Timestamp': timestamps,
    'Equipment_ID': equipment_ids,
    'Corrosion_Level': corrosion_levels,
    'Temperature': temperatures,
    'Pressure': pressures,
    'Humidity': humidity,
    'Weather_Condition': weather_conditions,
    'NDT_Result': ndt_results
})

# Save the DataFrame to a CSV file
data.to_csv('oil_gas_corrosion_data.csv', index=False)

# Optionally, save equipment master data to a CSV file
equipment_master.to_csv('equipment_master_data.csv', index=False)

print("Sample data generated and saved to 'oil_gas_corrosion_data.csv'")
print("Equipment master data saved to 'equipment_master_data.csv'")
