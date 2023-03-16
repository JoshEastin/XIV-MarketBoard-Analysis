import asyncio
import logging
import aiohttp
import json
import pandas as pd
import Functions as mb

WORLD = 'Excalibur'
ITEM_LEVEL = 620

print('Running ID List function')
dict_of_ids = asyncio.run(mb.SearchItems(ITEM_LEVEL))
#print(dict_of_ids)

#print("Attaching names to ID")
#asyncio.get_event_loop().run_until_complete(mb.convert_ids(dict_of_ids))

print('Running Price List function')
mb.FetchMBCurrentPrice(dict_of_ids, WORLD)

print('Running Sale History Function')
mb.FetchMBSaleHistory(dict_of_ids, WORLD, 2)

print(dict_of_ids)

mb.DrawBarGraph(dict_of_ids)
