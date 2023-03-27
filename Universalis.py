import requests
import os
import Files
EPOCH_DAY = 86400
SEVEN_DAYS_MS = 604800000

def CreateStringOfIDs(dict):
    myString = ''
    i = 0
    for x in range(len(dict)):
        i += i
        if(i < 100):
            myString += str(dict[x]['ID']) + ','

    myString = myString.rstrip(myString[-1])

    return myString

def FetchMBCurrentPrice(id_dict, world):
    
    idString = CreateStringOfIDs(id_dict)
    
    for x in range(len(id_dict)):
        response = requests.get(
            'https://universalis.app/api/v2/' + world + '/' + idString + '?listings=1')
        a = response.json()

        for y in range(len(a)):
            Files.WriteJSONFile(a['items'], 'test4')
            if(a['items'][str(id_dict[x]['ID'])]['listings'] != []):
                id_dict[x].update(pricePerUnit = a['items'][str(id_dict[x]['ID'])]['listings'][0]['pricePerUnit'])
            else:
                id_dict[x].update(pricePerUnit = 0)

def FetchMarketableItems():
    response = requests.get('https://universalis.app/api/v2/marketable').json()
    return response

def FetchMBSaleHistory(id_dict, world, sales=200, statsWithin=SEVEN_DAYS_MS, entriesWithin=(EPOCH_DAY * 1000)):

    idString = CreateStringOfIDs(id_dict)
    response = requests.get(
    'https://universalis.app/api/v2/history/' + world + '/' + idString + '?entriesToReturn=' + str(sales) + '&statsWithin=' + str(statsWithin) + '&entriesWithin=' + str(entriesWithin))

    a = response.json()

    if(len(id_dict) <= 100):
        for x in range(len(id_dict)):
            numOfSales = len(a['items'][str(a['itemIDs'][x])]['entries'])
            sum = 0
            quantitySold = 0
            for z in range(numOfSales):
                sum += a['items'][str(a['itemIDs'][x])]['entries'][z]['pricePerUnit']
                quantitySold += a['items'][str(a['itemIDs'][x])]['entries'][z]['quantity']
            average = sum / sales
            id_dict[x].update(Average_Price = average)
            id_dict[x].update(Market_Volume = average * quantitySold)
    else:
        for x in range(100):
            numOfSales = len(a['items'][str(a['itemIDs'][x])]['entries'])
            sum = 0
            quantitySold = 0
            for z in range(numOfSales):
                sum += a['items'][str(a['itemIDs'][x])]['entries'][z]['pricePerUnit']
                quantitySold += a['items'][str(a['itemIDs'][x])]['entries'][z]['quantity']
            average = sum / sales
            id_dict[x].update(Average_Price = average)
            id_dict[x].update(Market_Volume = average * quantitySold)

#async def SearchItems(itemLevel = 0):
    #filterList = [Filter("LevelItem", "gte", itemLevel)]
    #item = await client.index_search(
        #name="*",
        #indexes=["Item"],
        #filters=filterList,
        #per_page=10000,
        #columns=['ID', 'Name']
    #)

    #my_dict = item['Results']
    #my_list = []
    #marketable_items = FetchMarketableItems()
    #for x in range(len(my_dict)):
        #if(marketable_items.count(my_dict[x]['ID']) > 0):
            #my_list.append(my_dict[x])

    #await client.session.close()
    #return my_list

#async def convert_ids(id_dict):
#    
#    for x in range(len(id_dict)):
#        item = await client.index_by_id(
#            index="Item",
#            content_id=id_dict[x][0],
#            columns=["Name"]
#        )
#
#        id_dict[x].append(item['Name'])
#
#    await client.session.close()