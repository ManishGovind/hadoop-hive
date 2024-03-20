#!/usr/bin/env python3

import sys
import os
from datetime import datetime

# Get the environment variables for the desired parameters

location = os.getenv("location")
start_date = datetime.strptime(os.getenv("start_date"), "%Y%m%d")
end_date = datetime.strptime(os.getenv("end_date"), "%Y%m%d")
aggregation_unit = os.getenv("aggregation_unit")


for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split(',')

    # Extract relevant fields
    station_id = fields[0]
    date = datetime.strptime(fields[1], "%Y%m%d")
    temperature_type = fields[2]
    temperature_value = fields[3]

    # Check if the record is within the desired time period, location, and temperature type
    if start_date <= date <= end_date and fields[3] == location:
        # Emit key-value pairs: (key, temperature)
        if aggregation_unit == "year":
            key = f"{station_id}\t{date[:4]}"
        elif aggregation_unit == "month":
            key = f"{station_id}\t{date[:6]}"
        elif aggregation_unit == "day":
            key = f"{station_id}\t{date}"

        print(f"{key}\t{temperature_type}\t{temperature_value}")
