import csv
import json

csvFilePath = 'imdb_mbappe.csv'
jsonFilePath = 'json_file.json'

data = {"Mbappe_goal":{}}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    i = 0
    for rows in csvReader:
        id = i
        data["Mbappe_goal"][id] = rows
        i += 1

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))