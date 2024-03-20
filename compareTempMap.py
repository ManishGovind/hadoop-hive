#!/usr/bin/env python3

import sys
import os

# Get the environment variable for the region to compare
region_to_compare = os.getenv("region_to_compare")

for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split(',')

    # Extract relevant fields
    location = fields[3]
    date = fields[1]
    temperature_type = fields[2]
    temperature_value = fields[4]

    # Check if the record is for the desired region and temperature type
    if location == region_to_compare:
        # Emit key-value pairs: (date, temperature_type), temperature_value
        print(f"{date}\t{temperature_type}\t{temperature_value}")
