import asyncio
import pyxivapi
from pyxivapi.models import Filter, Sort
import requests
from collections import defaultdict

client = pyxivapi.XIVAPIClient(api_key="--API key goes here--")

def fetch_most_sold_ids():
    response = requests.get('https://universalis.app/api/v2/extra/stats/most-recently-updated?world=Excalibur&entries=20')
    a = response.json()
    my_dict = {}

    collect = defaultdict(dict)
    x = 0
    for key in a['items']:
        my_dict[x]=[key['itemID']]
        x += 1
        
    return my_dict

def fetch_mb_data(id_dict, world, listings=1):
    for x in range(len(id_dict)):
        #print('Fetching from https://universalis.app/api/v2/' + world + '/' + str(id_dict[x][0]) + '?listings=' + str(listings))
        response = requests.get(
            'https://universalis.app/api/v2/' + world + '/' + str(id_dict[x][0]) + '?listings=' + str(listings))
        a = response.json()

        collect = defaultdict(dict)
        for key in a['listings']:
            id_dict[x].append(key['pricePerUnit'])

def fetch_marketable_items():
    response = requests.get('https://universalis.app/api/v2/marketable').json()
    return response

def fetch_mb_sale_history(id_dict, world, sales=100):
    for x in range(len(id_dict)):
        #print('Fetching from https://universalis.app/api/v2/history/' + world + '/' + str(id_dict[x][0]) + '?entriesToReturn=' + str(sales))
        response = requests.get(
            'https://universalis.app/api/v2/history/' + world + '/' + str(id_dict[x][0]) + '?entriesToReturn=' + str(sales))

    a = response.json()
    
    collect = defaultdict(dict)
    sum = 0
    #print("a['entries']" + str(a['entries']))
    for x in range(len(id_dict)):
        for y in range(len(id_dict)):
            sum += a['entries'][y]['pricePerUnit']
        average = sum / sales

        id_dict[x].append(average)

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

async def convert_ids(id_dict):
    
    for x in range(len(id_dict)):
        item = await client.index_by_id(
            index="Item",
            content_id=id_dict[x][0],
            columns=["Name"]
        )

        id_dict[x].append(item['Name'])

    await client.session.close()