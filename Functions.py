import asyncio
import pyxivapi
from pyxivapi.models import Filter, Sort
import requests
from collections import defaultdict
import pandas as pd
from matplotlib import pyplot as plt
from dotenv import load_dotenv
import os
import json
import math

load_dotenv()
apiKey = os.getenv('api_key')
client = pyxivapi.XIVAPIClient(api_key=apiKey)

def DrawBarGraph(list):
    data = pd.DataFrame(list)
    data_sorted = data.sort_values('Average_Price')

    name = data_sorted['Name']
    averagePrice = data_sorted['Average_Price']

    fix, ax = plt.subplots(figsize =(16,9))

    ax.barh(name, averagePrice)

    plt.xlabel('Average Gil Value (Millions)')
    plt.title('Average Gil Value by Item')

    plt.tight_layout()

    plt.show()

def CreateStringOfIDs(dict):
    myString = ''
    i = 0
    for x in range(len(dict)):
        i += i
        if(i < 100):
            myString += str(dict[x]['ID']) + ','

    myString = myString.rstrip(myString[-1])

    return myString

#Deprecated. Functionality proved useless to the program as it returned random items
#def FetchMostRecentIDs():
    #response = requests.get('https://universalis.app/api/v2/extra/stats/most-recently-updated?world=Excalibur&entries=20')
    #a = response.json()
    #my_dict = {}

    #collect = defaultdict(dict)
    #x = 0
    #for key in a['items']:
        #my_dict[x]=[key['itemID']]
        #x += 1
        
    return my_dict

def FetchMBCurrentPrice(id_dict, world, listings=1):
    
    idString = CreateStringOfIDs(id_dict)
    response = requests.get(
        'https://universalis.app/api/v2/' + world + '/' + idString + '?listings=' + str(listings))
    a = response.json()

    #print(range(len(id_dict)))
    #print(id_dict)
    for x in range(len(id_dict)):
        #if(a['items'][str(a['itemIDs'][x])]['listings'][0] != []):
        
        #print("a['items'][str(id_dict[" + str(x) + "]['ID'])]['listings'][0]['pricePerUnit] = " + str(a['items'][str(id_dict[x]['ID'])]['listings'][0]['pricePerUnit']))
        for x in range(len(a)):
            if(a['items'][str(id_dict[x]['ID'])]['listings'] != []):
                id_dict[x].update(pricePerUnit = a['items'][str(id_dict[x]['ID'])]['listings'][0]['pricePerUnit'])
            else:
                id_dict[x].update(pricePerUnit = 0)
        #print(id_dict[x])

def fetch_marketable_items():
    response = requests.get('https://universalis.app/api/v2/marketable').json()
    return response

def FetchMBSaleHistory(id_dict, world, sales=10):

    idString = CreateStringOfIDs(id_dict)
    response = requests.get(
    'https://universalis.app/api/v2/history/' + world + '/' + idString + '?entriesToReturn=' + str(sales))

    a = response.json()
    if len(id_dict) <= 100:
        for x in range(len(id_dict)):
            sum = 0
            for z in range(sales):
                sum += a['items'][str(a['itemIDs'][x])]['entries'][z]['pricePerUnit']
            average = sum / sales
            id_dict[x].update(Average_Price = average)
    else:
        for x in range(100):
            sum = 0
            for z in range(sales):
                sum += a['items'][str(a['itemIDs'][x])]['entries'][z]['pricePerUnit']
            average = sum / sales
            id_dict[x].update(Average_Price = average)

async def SearchItems(itemLevel = 0):
    filterList = [Filter("LevelItem", "gte", itemLevel)]
    item = await client.index_search(
        name="*",
        indexes=["Item"],
        filters=filterList,
        per_page=10000,
        columns=['ID', 'Name']
    )

    my_dict = item['Results']
    my_list = []
    marketable_items = fetch_marketable_items()
    for x in range(len(my_dict)):
        if(marketable_items.count(my_dict[x]['ID']) > 0):
            my_list.append(my_dict[x])

    await client.session.close()
    return my_list

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