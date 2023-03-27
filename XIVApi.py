import requests
import Files

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

