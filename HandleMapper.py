#!/usr/bin/env python3

import sys

# Function to check if the station is located in North America
def is_north_america(country_code):
    return country_code in ['US', 'CA', 'MX']

for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split(',')

    # Extract relevant fields
    station_id = fields[0][:11]
    date = fields[1]
    element = fields[2]
    data_value = fields[3]
    country_code = station_id[:2]

    # Check if the station is in North America
    if is_north_america(country_code):
        # Emit key-value pairs: (station_id, date), (element, data_value)
        key = station_id  + '_' + date
        print(f"{key},{element},{data_value},{country_code}")
