import pandas as pd
from matplotlib import pyplot as plt

def DrawBarGraph(list):
    data = pd.DataFrame(list)
    data_sorted = data.sort_values('Market_Volume')

    name = data_sorted['Name']
    marketVolume = data_sorted['Market_Volume']

    fix, ax = plt.subplots(figsize =(16,9))

    ax.barh(name, marketVolume)

    plt.xlabel('Gil (Millions)')
    plt.title('Market Volume by Item')

    plt.tight_layout()

    plt.show()