#!/usr/bin/env python3

import sys

current_key = None
current_tmin_values = []
current_tmax_values = []
current_tavg_values = []

def calculate_average(values):
    if values:
        return sum(map(float, values)) / len(values)
    else:
        return 'NAN'

for line in sys.stdin:
    # Split the input line into key and value
    key, temperature_type, temperature = line.strip().split('\t')

    # Check if the key has changed
    if current_key != key:
        # If it's not the first line, emit the result
        if current_key is not None:
            avg_tmin = calculate_average(current_tmin_values)
            avg_tmax = calculate_average(current_tmax_values)
            avg_tavg = calculate_average(current_tavg_values)

            print(f"{current_key},{avg_tmin},{avg_tmax},{avg_tavg}")

        # Reset for the new key
        current_key = key
        current_tmin_values = []
        current_tmax_values = []
        current_tavg_values = []

    # Add the temperature to the respective lists based on the temperature type
    if temperature_type == 'TMIN':
        current_tmin_values.append(temperature)
    elif temperature_type == 'TMAX':
        current_tmax_values.append(temperature)
    elif temperature_type == 'TAVG':
        current_tavg_values.append(temperature)

# Output the last key's result
if current_key is not None:
    avg_tmin = calculate_average(current_tmin_values)
    avg_tmax = calculate_average(current_tmax_values)
    avg_tavg = calculate_average(current_tavg_values)

    print(f"{current_key},{avg_tmin},{avg_tmax},{avg_tavg}")
