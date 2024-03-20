#!/usr/bin/env python3

import sys



# Function to impute missing temperature values based on available data
def impute_missing_temperature(tmin, tmax, tavg):
    if tmin == 'NAN' and tmax and tavg:
        tmin = 2 * float(tavg) - float(tmax)
    elif tmax == 'NAN' and tmin and tavg:
        tmax = 2 * float(tavg) - float(tmin)
    elif tavg == 'NAN' and tmin and tmax:
        tavg = (float(tmin) + float(tmax)) // 2

    return tmin, tmax, tavg

def print_records(data):
    tmin, tmax, tavg = "NAN", "NAN", "NAN"
    
    for row in data:
        if row[2] == "TMIN":
            tmin = row[3]
        elif row[2] == "TMAX":
            tmax = row[3]
        elif row[2] == "TAVG":
            tavg = row[3]

    tmin, tmax, tavg = impute_missing_temperature(tmin, tmax, tavg)

    for row in data:
        row[3] = tmin if row[2] == "TMIN" else tmax if row[2] == "TMAX" else tavg  if row[2] == "TAVG" else row[3]
        print(f"{row[0]},{row[1]},{row[2]},{row[3]}")



current_key = None
data_records = []

for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split('\t')

    # Extract relevant fields
    key = fields[0]
    station_id, date = key.split('_')
    element = fields[2]
    data_value = fields[3]

    if current_key != key:
        # Impute missing temperature values based on available data
        if current_key is not None and data_records:
            print_records(data_records)

        current_key = key
        data_records = []


    data_records.append([station_id, date, element, data_value])

# Check for the last station in the input
if current_key is not None and data_records:
        print_records(data_records)
    
