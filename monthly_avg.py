import csv
from statistics import mean
# this makes mean() work
# instead of import statistics :  statistics.mean()
import os

with open("./folder/FL_insurance_sample.csv") as f:
    reader = csv.reader(f)

    hu_site_limits = []
    site_limits = []
    for row in reader:
        hu_site_limits.append(row[4])

    for i in range(len(hu_site_limits)):
        if i != 0:
            site_limits.append(
                float(hu_site_limits[i]) - float(hu_site_limits[i-1]))

    max_limit = max(site_limits)
    min_limit = min(site_limits)
    avg_site_limit = mean(site_limits)


print(avg_site_limit)
