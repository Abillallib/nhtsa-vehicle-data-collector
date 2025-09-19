# NHTSA Vehicle Data Collector

This repository contains a Python workflow to automatically collect vehicle data from the NHTSA Vehicle API and prepare it for local database ingestion.

# Key Features

Automated Data Collection
- Retrieves all vehicle makes, models, and model years from the NHTSA API.

Duty Type Inference
- Classifies vehicles as Heavy-Duty or Light-Duty based on keywords in make and model names.

Data Output
- Generates a CSV file with the following columns: Duty Type, Make, Model, Model Year.
- Ready for normalization and integration into local company databases or analytics workflows.

Progress and Rate Limiting
- Provides progress bars using tqdm.
- Includes delay to avoid hitting API rate limits.
