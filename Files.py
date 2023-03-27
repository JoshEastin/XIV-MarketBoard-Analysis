import json
import csv
from csv import DictReader

def WriteJSONFile(input, fileName='noName'):
    json_object = json.dumps(input, indent=4)
    with open(fileName + '.json', 'w') as outfile:
        outfile.write(json_object)

def WriteDictToCSVFile(input, fileName='noName'):
    myFile = open('Lists/' + fileName + '.csv', 'w')
    writer = csv.DictWriter(myFile, fieldnames=['Name', 'ID'])
    writer.writeheader()
    writer.writerows(input)
    myFile.close()

def ReadDictFromCSVFile(fileName):
    with open('Lists/' + fileName + '.csv', newline='') as csvfile:
        dict_reader = DictReader(csvfile)
        output = list(dict_reader)
        return(output)
