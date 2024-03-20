#!/usr/bin/env python3

import sys

current_key = None
region_values = {'Region1': {}, 'Region2': {}}

for line in sys.stdin:
    # Split the input line into key and value
    date, temperature_type, temperature_value = line.strip().split('\t')

    # Check if the key has changed
    if current_key != date:
        # If it's not the first line, emit the result
        if current_key is not None:
            region1_value = region_values['Region1'].get(temperature_type, 'NAN')
            region2_value = region_values['Region2'].get(temperature_type, 'NAN')

            # Emit key-value pairs: (date, temperature_type), region1_value, region2_value, difference
            print(f"{current_key}\t{temperature_type}\t{region1_value}\t{region2_value}\t{float(region1_value) - float(region2_value)}")

        # Reset for the new key
        current_key = date
        region_values = {'Region1': {}, 'Region2': {}}

    # Add the temperature value to the respective region dictionary
    region_values[temperature_type][f"Region{current_region}"] = temperature_value

# Output the last key's result
if current_key is not None:
    region1_value = region_values['Region1'].get(temperature_type, 'NAN')
    region2_value = region_values['Region2'].get(temperature_type, 'NAN')

    # Emit key-value pairs: (date, temperature_type), region1_value, region2_value, difference
    print(f"{current_key}\t{temperature_type}\t{region1_value}\t{region2_value}\t{float(region1_value) - float(region2_value)}")
