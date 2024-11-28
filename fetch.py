import requests
import pandas as pd

try:
    # Fetch waste items data
    waste_response = requests.get('http://127.0.0.1:8000/waste_items')
    waste_response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    waste_data = waste_response.json()  # Parse JSON response

    # Fetch waste collectors data
    collectors_response = requests.get('http://127.0.0.1:8000/waste_collectors')
    collectors_response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    collectors_data = collectors_response.json()  # Parse JSON response

    # Convert JSON data into pandas DataFrames
    waste_df = pd.DataFrame(waste_data)  # Assumes waste_data is a list of dicts
    collectors_df = pd.DataFrame(collectors_data)  # Assumes collectors_data is a list of dicts

    # Ensure the `waste_df` has a column to match with `collectors_df`
    if 'assigned_collector_id' in waste_df.columns and 'id' in collectors_df.columns:
        merged_df = pd.merge(
            waste_df,
            collectors_df,
            left_on='assigned_collector_id',
            right_on='id',
            suffixes=('_waste', '_collector')
        )

        print("Merged DataFrame:")
        print(merged_df)
    else:
        print("Cannot merge: Missing common columns (`assigned_collector_id` in waste_df or `id` in collectors_df).")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
except ValueError as ve:
    print(f"Error processing data: {ve}")
