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

csvfile_confirmed_global = open('time_series_covid19_confirmed_global.csv', 'r')
csvfile_confirmed_US = open('time_series_covid19_confirmed_US.csv', 'r')
jsonfile = open('globe/covid19_confirmed.json', 'w')

jsonfile.write('[\n')

# write global confirmed cases data to json
jsonfile.write('    [\n    \"Confirmed\", [')

reader = csv.DictReader(csvfile_confirmed_global)
rows = []
for row in reader:
    if row.get('Country/Region') == 'US':
        continue # omit US (added separately)
    cases = float(row.get(next(reversed(row))))
    coords = [row.get('Lat'), row.get('Long')]
    if coords == ['', '']:
        coords = ['0', '0']
    s = coords[0] + ', ' + coords[1] + ', ' + str(scale(cases))
    rows.append(s)
t = ', '.join(rows)
jsonfile.write(t)

jsonfile.write(', ')

# write US confirmed cases data to json
reader = csv.DictReader(csvfile_confirmed_US)
rows = []
for row in reader:
    cases = float(row.get(next(reversed(row))))
    coords = [row.get('Lat'), row.get('Long_')]
    if coords == ['', '']:
        coords = ['0', '0']
    s = coords[0] + ', ' + coords[1] + ', ' + str(scale(cases))
    rows.append(s)
t = ', '.join(rows)
jsonfile.write(t)

jsonfile.write(']\n    ]\n')

jsonfile.write(']')

csvfile_confirmed_global.close()
csvfile_confirmed_US.close()
jsonfile.close()