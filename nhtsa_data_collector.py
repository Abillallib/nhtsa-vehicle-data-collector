import requests
import os
import pandas as pd
from tqdm import tqdm
import time

# Get all vehicle makes
makes_url = "https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json"
makes_response = requests.get(makes_url)
makes = makes_response.json()['Results']

# Prepare a list to store the data
vehicle_data = []

# Helper function to infer duty type based on keywords
def infer_duty_type(make_name, model_name):
    heavy_keywords = ['Truck', 'Bus', 'Van', 'Trailer', 'Commercial']
    if any(keyword.lower() in (make_name + model_name).lower() for keyword in heavy_keywords):
        return 'Heavy-Duty'
    return 'Light-Duty'

# For each make, retrieve models and years
for make in tqdm(makes): 
    make_id = make['Make_ID']
    make_name = make['Make_Name']
    models_url = f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/{make_id}?format=json"
    models_response = requests.get(models_url)
    models = models_response.json()['Results']

    for model in models:
        model_name = model['Model_Name']
        # Assuming model years from 2020 to 2025 for demo
        for year in range(2020, 2025):
            duty_type = infer_duty_type(make_name, model_name)
            vehicle_data.append([duty_type, make_name, model_name, year])
    time.sleep(0.5)  # To avoid hitting rate limits

# Create DataFrame and export to CSV in Downloads folder
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "all_vehicles_nhtsa.csv")
df = pd.DataFrame(vehicle_data, columns=['Duty Type', 'Make', 'Model', 'Model Year'])
df.to_csv(downloads_path, index=False)
print(f"Data saved to '{downloads_path}'")
