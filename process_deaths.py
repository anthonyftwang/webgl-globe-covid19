import csv
import json
import math

LOG_DEVIATION = 0.45 # valid on 0<n<1: 0 => log(x), 1 => xlog(x)
LIN_SCALING = 0.00025

def scale(cases):
    if cases < 0: # domain{log(x+1)}
        cases = 0
    z = ((cases**LOG_DEVIATION)*(math.log(cases+1)))
    return (z * LIN_SCALING)

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
    cases = float(row.get(next(reversed(row))))
    s = row.get('Lat') + ', ' + row.get('Long') + ', ' + str(scale(cases))
    rows.append(s)
t = ', '.join(rows)
jsonfile.write(t)

jsonfile.write(', ')

# write US deaths cases data to json
reader = csv.DictReader(csvfile_deaths_US)
rows = []
for row in reader:
    cases = float(row.get(next(reversed(row))))
    s = row.get('Lat') + ', ' + row.get('Long_') + ', ' + str(scale(cases))
    rows.append(s)
t = ', '.join(rows)
jsonfile.write(t)

jsonfile.write(']\n    ]\n')

jsonfile.write(']')

csvfile_deaths_global.close()
csvfile_deaths_US.close()
jsonfile.close()