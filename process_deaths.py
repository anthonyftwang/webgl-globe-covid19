import csv
import json
import math

csvfile_deaths_global = open('time_series_covid19_deaths_global.csv', 'r')
csvfile_deaths_US = open('time_series_covid19_deaths_US.csv', 'r')
jsonfile = open('globe/covid19_deaths.json', 'w')

jsonfile.write('[\n')

# write global deaths cases data to json
jsonfile.write('    [\n    \"Deaths\", [')

reader = csv.DictReader(csvfile_deaths_global)
rows = []
for row in reader:
    if row.get('Country/Region') == 'US':
        continue # omit US (added separately)
    if float(row.get(next(reversed(row)))) < 0:
        cases = 0 # guarantee normalization works (use 1s for logarithmic)
    else:
        cases = float(row.get(next(reversed(row))))
    s = row.get('Lat') + ', ' + row.get('Long') + ', ' + str((cases**0.4)*0.01) # improves viewability
    rows.append(s)
s = ', '.join(rows)
jsonfile.write(s)

jsonfile.write(', ')

# write US deaths cases data to json
reader = csv.DictReader(csvfile_deaths_US)
rows = []
for row in reader:
    if float(row.get(next(reversed(row)))) < 0:
        cases = 0 # guarantee normalization works (use 1s for logarithmic)
    else:
        cases = float(row.get(next(reversed(row))))
    s = row.get('Lat') + ', ' + row.get('Long_') + ', ' + str((cases**0.4)*0.01) # improves viewability
    rows.append(s)
s = ', '.join(rows)
jsonfile.write(s)

jsonfile.write(']\n    ]\n')

jsonfile.write(']')

csvfile_deaths_global.close()
csvfile_deaths_US.close()
jsonfile.close()

