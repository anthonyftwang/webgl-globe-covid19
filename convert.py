import csv
import json

csvfile_confirmed = open('time_series_covid19_confirmed_global.csv', 'r')
csvfile_deaths = open('time_series_covid19_deaths_global.csv', 'r')
jsonfile = open('globe-covid19/covid19.json', 'w')

jsonfile.write('[\n')

# write confirmed cases data to json
jsonfile.write('    [\n    \"Confirmed\", [')

reader = csv.DictReader(csvfile_confirmed)
rows = []
for row in reader:
    s = row.get('Lat') + ', ' + row.get('Long') + ', ' + row.get(next(reversed(row)))
    rows.append(s)
s = ', '.join(rows)
jsonfile.write(s)

jsonfile.write(']\n    ],\n')

# write deaths data to json
jsonfile.write('    [\n    \"Deaths\", [')

reader = csv.DictReader(csvfile_deaths)
rows = []
for row in reader:
    s = row.get('Lat') + ', ' + row.get('Long') + ', ' + row.get(next(reversed(row)))
    rows.append(s)
s = ', '.join(rows)
jsonfile.write(s)

jsonfile.write(']\n    ]\n')

jsonfile.write(']')

