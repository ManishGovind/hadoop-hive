#!/usr/bin/env python3

import sys

current_key = None
data = []
elements = ['TMIN', 'TMAX', 'TAVG', 'PRCP']
def print_records(data):
      elements_exist  = [record[3] for record in data]
      for ele in elements :
        if len(data) > 0 and ele not in elements_exist:
            print(f"{data[0][0]},{data[0][1]},{ele},NAN,{data[0][3]}")
        
      for record in data:
            print(f"{record[0]},{record[1]},{record[2]},{record[3]}")


for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split('\t')

    # Extract relevant fields
    key = fields[0]
    station_id, date = key.split('_')
    element = fields[1]
    data_value = fields[2]

    if current_key != key:
        # If this is not the first record,
        if current_key is not None:
            print_records(data)

        current_key = key
        data = []

    data.append([station_id,date,element,data_value])
   

# Check for the last station in the input
if current_key is not None:
    print_records(data)