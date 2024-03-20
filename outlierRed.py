#!/usr/bin/env python3

import sys
# Function to check if a value is a valid float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False



# Function to check if a station has more than 10 consecutive missing days
def has_consecutive_missing_days(days):
    consecutive_missing_count = 0
    for day in days:
        if day == 'NAN':
            consecutive_missing_count += 1
            if consecutive_missing_count > 10:
                return True
        else:
            consecutive_missing_count = 0
    return False

# Function to impute outliers by taking the average of the previous and following three days
def impute_outlier(data_values):
    imputed_values = []
    for i, value in enumerate(data_values):
        if value == 'NAN':
            previous_values = [data_values[j] for j in range(max(0, i - 3), i) if data_values[j]]
            following_values = [data_values[j] for j in range(i + 1, min(len(data_values), i + 4)) if data_values[j]]

            if previous_values and following_values:
                avg_value = (sum(previous_values) + sum(following_values)) / (len(previous_values) + len(following_values))
                imputed_values.append(str(avg_value))
            elif previous_values:
                imputed_values.append(str(sum(previous_values) / len(previous_values)))
            elif following_values:
                imputed_values.append(str(sum(following_values) / len(following_values)))
            else:
                imputed_values.append('NAN')
        else:
            imputed_values.append(value)
    return imputed_values

def print_records(data):
    imputed_tmin_data_values = impute_outlier([record[3] for record in data if record[2] == "TMIN"] )
    imputed_tmax_data_values = impute_outlier([record[3] for record in data if record[2] == "TMAX"] )
    imputed_prep_data_values =  impute_outlier([record[3] for record in data if record[2] == "PRCP"] )
    for i, record in enumerate(data):
        if record[2] == 'TMIN'  and record[3] =="NAN" :
            val = imputed_tmin_data_values[i]
        if record[2] == 'TMAX'  and record[3] =="NAN" :
            val = imputed_tmax_data_values[i] 
        if record[2] == 'PRCP'  and record[3] =="NAN" :
            val = imputed_prep_data_values[i]

        record[3] = val
        print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}")

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
    country =  fields[4]

    if current_key != station_id:
        # Check for consecutive missing days and exclude the station if needed
        if current_key is not None and not has_consecutive_missing_days([record[3] for record in data_records]):
            
            print_records(data_records)

        current_key = station_id
        data_records = []

    data_records.append([station_id, date, element, data_value , country])

# Check for the last station in the input
if current_key is not None and not has_consecutive_missing_days([record[3] for record in data_records]):
    print_records(data_records)
