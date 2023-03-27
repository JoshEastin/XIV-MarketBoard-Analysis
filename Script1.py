import Universalis
import XIVApi
import Graph
import Files

WORLD = 'Excalibur'
ITEM_LEVEL = 610

# userDefinedList = XIVApi.SearchIDByName(
#     [{'Name': 'Carrot Pudding'}, {'Name': 'Garlean Pizza'}, {'Name': 'Gyros'}, 
#      {'Name': 'Jhinga Biryani'}, {'Name': 'Jhinga Curry'}, {'Name': 'King Urchin Loaf'}, 
#      {'Name': 'Loaghtan Rump Steak'}, {'Name': 'Melon Juice'}, {'Name': 'Melon Pie'}, 
#      {'Name': 'Piennolo Tomato Salad'}, {'Name': 'Sunset Carrot Nibbles'}, {'Name': 'Urchin Pasta'},
#      {'Name': 'Grade 7 Tincture of Dexterity'}, {'Name': 'Grade 7 Tincture of Intelligence'}, 
#      {'Name': 'Grade 7 Tincture of Mind'}, {'Name': 'Grade 7 Tincture of Strength'}, 
#      {'Name': 'Grade 7 Tincture of Vitality'}], 'RaidFood')

userDefinedList = Files.ReadDictFromCSVFile('RaidFood')

print('Running Price List function')
Universalis.FetchMBCurrentPrice(userDefinedList, WORLD)

print('Running Sale History Function')
Universalis.FetchMBSaleHistory(userDefinedList, WORLD)

print(userDefinedList)

Graph.DrawBarGraph(userDefinedList)