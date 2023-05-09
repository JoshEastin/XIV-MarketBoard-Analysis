import Functions.Universalis as Universalis
import Functions.XIVApi as XIVApi
import Functions.Graph as Graph
import Functions.Files as Files
import Functions.GUI as GUI

WORLD = 'Excalibur'
ITEM_LEVEL = 610

def main(world=WORLD, fileName='RaidFood'):
    print(world)
    userDefinedList = Files.ReadDictFromCSVFile(fileName)

    print('Running Price List function')
    Universalis.FetchMBCurrentPrice(userDefinedList, world)

    print('Running Sale History Function')
    Universalis.FetchMBSaleHistory(userDefinedList, world, 500)

    print(userDefinedList)

    Graph.DrawBarGraph(userDefinedList, world)

# userDefinedList = XIVApi.SearchIDByName(
#     [{'Name': 'Carrot Pudding'}, {'Name': 'Garlean Pizza'}, {'Name': 'Gyros'}, 
#      {'Name': 'Jhinga Biryani'}, {'Name': 'Jhinga Curry'}, {'Name': 'King Urchin Loaf'}, 
#      {'Name': 'Loaghtan Rump Steak'}, {'Name': 'Melon Juice'}, {'Name': 'Melon Pie'}, 
#      {'Name': 'Piennolo Tomato Salad'}, {'Name': 'Sunset Carrot Nibbles'}, {'Name': 'Urchin Pasta'},
#      {'Name': 'Grade 7 Tincture of Dexterity'}, {'Name': 'Grade 7 Tincture of Intelligence'}, 
#      {'Name': 'Grade 7 Tincture of Mind'}, {'Name': 'Grade 7 Tincture of Strength'}, 
#      {'Name': 'Grade 7 Tincture of Vitality'}], 'RaidFood')