import requests
import Functions.Files as Files

def SearchIDByName(namesDict, fileName):

    for dictEntry in namesDict:
        response=requests.get(
            'https://xivapi.com/search?String=' + dictEntry['Name']
        )

        a = response.json()

        IDOfItem = ''

        for x in a['Results']:
            if(x['UrlType'] == 'Item'):
                IDOfItem = str(x['ID'])

        dictEntry.update(ID = IDOfItem)

    Files.WriteDictToCSVFile(namesDict, fileName)
    return(namesDict)

def SearchByString(string, fileName):
    response=requests.get('https://xivapi.com/search?String=' + string + '&columns=Name,ID')

    a = response.json()

    listOfItems = []

    iteration = 0
    for searchResult in a['Results']:
        dict = {'Name': a['Results'][iteration]['Name'], 'ID': a['Results'][iteration]['ID']}
        listOfItems.append(dict)
        iteration += 1

    Files.WriteDictToCSVFile(listOfItems, fileName)