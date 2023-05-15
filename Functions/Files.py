import json
import csv
from csv import DictReader
import os

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
    
def GenerateListOfCSVFiles():
    cwdPath = os.getcwd()
    parentPath = os.path.join(cwdPath, os.pardir)
    parentPath = parentPath[:-2]
    listsPath = parentPath + 'Lists'
    folderList = []
    for x in os.listdir(listsPath):
        if x.endswith('.csv'):
            folderList.append(x[:-4])
            
    return folderList
