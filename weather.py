from pyhive import hive
import pandas as pd

# Establish a connection to Hive
conn = hive.connect(host='your_hive_server', port=10000, username='your_username')

# Define the location, threshold, and temperature type
location = 'Your_Location'
heatwave_threshold = 30  # Example threshold for a heatwave, adjust as needed
cold_spell_threshold = 10  # Example threshold for a cold spell, adjust as needed
temperature_type = 'TMAX'  # Adjust based on your requirement

# HiveQL query to identify heatwaves
heatwave_query = f"""
    SELECT station_id, date, temperature_type, temperature_value
    FROM temperature_data
    WHERE temperature_type = '{temperature_type}'
        AND temperature_value > {heatwave_threshold}
        AND location = '{location}'
"""

# Execute the query and fetch results into a DataFrame
heatwave_df = pd.read_sql(heatwave_query, conn)

# Identify consecutive days for heatwaves
heatwave_df['date'] = pd.to_datetime(heatwave_df['date'])
heatwave_df['consecutive_days'] = (heatwave_df['date'] - heatwave_df['date'].shift(1)).dt.days.ne(1).cumsum()

# Print the heatwave DataFrame
print(heatwave_df)
