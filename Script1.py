import asyncio
import logging
import aiohttp
import json
import pandas as pd
import Functions as mb

WORLD = 'Excalibur'
print('Running ID List function')
dict_of_ids = mb.fetch_most_sold_ids()
#print(dict_of_ids)

print("Attaching names to ID")
asyncio.get_event_loop().run_until_complete(mb.convert_ids(dict_of_ids))

print('Running Price List function')
mb.fetch_mb_data(dict_of_ids, WORLD)

print('Running Sale History Function')
mb.fetch_mb_sale_history(dict_of_ids, WORLD)


print(dict_of_ids)


print('Running Fetch MB Data function')
#print(mb.fetch_mb_data(dict_of_ids, WORLD))
