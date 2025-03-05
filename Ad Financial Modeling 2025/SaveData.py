import requests
import pandas as pd
import os

# Alpha Vantage API Key
API_KEY = "EYJDZ6HFWO4REUT1"

# Stock symbol (change this if needed)
STOCK_SYMBOL = "KO" 

# Define the folder to save the file
DATA_FOLDER = "data"

# Create the 'data' folder if it does not exist
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Alpha Vantage API URL
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={STOCK_SYMBOL}&apikey={API_KEY}&datatype=json"

# Fetch the data
response = requests.get(url)
data = response.json()

# Extract time series data
time_series = data.get("Weekly Adjusted Time Series", {})

# Convert data to DataFrame
df = pd.DataFrame.from_dict(time_series, orient="index")
df.index = pd.to_datetime(df.index)  # Convert index to datetime
df = df.sort_index()  # Sort by date (oldest to newest)

# Define CSV file path
csv_filename = os.path.join(DATA_FOLDER, f"{STOCK_SYMBOL}_weekly_adj_price.csv")

# Save DataFrame to CSV
df.to_csv(csv_filename)

print(f"Data saved successfully to {csv_filename}")
