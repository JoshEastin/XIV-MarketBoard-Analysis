import customtkinter
from customtkinter import *
import Functions.Files as Files
import Functions.XIVApi as XIVApi
import Functions.Universalis as Universalis
import Functions.Main as Main

worldList = ['Balmung','Behemoth','Brynhildr','Cactuar','Coeurl','Diabolos','Excalibur','Exodus','Faerie','Famfrit','Gilgamesh','Goblin','Halicarnassus','Hyperion','Jenova','Lamia','Leviathan','Maduin','Malboro','Marilith','Mateus','Midgardsormr','Sargatanas','Seraph','Siren','Ultros','Zalera']
filesList = Files.GenerateListOfCSVFiles()

class RunWindow(customtkinter.CTkFrame):
    def __init__(self, master):
        # ---Initialize Variables---
        self.world = StringVar()
        self.item = StringVar()

        # ---Initialize Frame to Hold Widgets---
        self.mainFrame = customtkinter.CTkFrame(master)
        self.mainFrame.pack(pady=20, padx=60, fill='both', expand=True)

        # ---Initialize Widgets---
        self.label = customtkinter.CTkLabel(master=self.mainFrame, text="XIV Market Volume")
        self.worldDropdown = customtkinter.CTkOptionMenu(master=self.mainFrame, width=170, variable=self.world, values=worldList)
        self.listsDropdown = customtkinter.CTkOptionMenu(master=self.mainFrame, width=130, variable=self.item, values=filesList)
        self.refreshButton = customtkinter.CTkButton(master=self.mainFrame, text='↺', width=20, command=lambda: self.updateLists())
        self.progressLabel = customtkinter.CTkLabel(master=self.mainFrame, text='')
        self.runButton = customtkinter.CTkButton(master=self.mainFrame, text="Run", width=170, command=lambda: Main.main(self.world.get(), self.item.get()))
        self.listButton = customtkinter.CTkButton(master=self.mainFrame, text="Create New List", width=170, command=lambda: self.openListWindow())

        # ---Place Widgets---
        self.label.grid(pady=12, padx=10, columnspan=2)
        self.worldDropdown.grid(pady=12, padx=20, columnspan=2)
        self.listsDropdown.grid(pady=12, padx=(20,0), row=2, column=0)
        self.refreshButton.grid(pady=12, padx=(10,20), row=2, column=1)
        self.runButton.grid(pady=12, padx=20, columnspan=2)
        self.listButton.grid(pady=12, padx=20, columnspan=2)

    def openListWindow(self):
        self.listWindow = ListWindow()
        self.listWindow.window.title('Create New List')
        self.listWindow.window.resizable(False,False)
        self.listWindow.window.mainloop()

    def updateLists(self):
        self.listsDropdown.configure(values=Files.GenerateListOfCSVFiles())

class ListWindow(customtkinter.CTkFrame):

    itemList = []

    def __init__(self):
        # ---Create Window---
        self.window = customtkinter.CTkToplevel()
        self.window.grab_set()

        # ---Initialize Frames to Hold Widgets---
        self.listFrame = customtkinter.CTkFrame(self.window)
        self.nameFrame = customtkinter.CTkFrame(self.window)
        
        self.listFrame.pack(pady=(20,6), padx=20, expand=True)
        self.nameFrame.pack(pady=(6,20), padx=20, expand=True)

        # ---Initialize Widgets---
        self.itemTutorialLabel = customtkinter.CTkLabel(master=self.listFrame, text="Add items to list:")
        self.entry = customtkinter.CTkEntry(master=self.listFrame, placeholder_text='Enter Item Name...')
        self.addButton = customtkinter.CTkButton(master=self.listFrame, text="Submit", width=50, command=lambda: self.addItemToList(self.entry.get()))
        self.label = customtkinter.CTkLabel(master=self.listFrame, text="Status:")
        self.statusLabel = customtkinter.CTkLabel(master=self.listFrame, text="")
        self.listCountLabel = customtkinter.CTkLabel(master=self.listFrame, text="0 items in list.")

        self.nameTutorialLabel = customtkinter.CTkLabel(master=self.nameFrame, text="Input list name when finished:")
        self.nameEntry = customtkinter.CTkEntry(master = self.nameFrame, placeholder_text="Enter Name of List...")
        self.submitButton = customtkinter.CTkButton(master=self.nameFrame, text="Submit", width=50, command=lambda: self.saveEntries(self.itemList, self.nameEntry.get()))

        # ---Place Widgets---
        self.itemTutorialLabel.grid(padx=12, pady=4, row=0, columnspan=2)
        self.entry.grid(padx=12, pady=(0, 12), row=1, column=0)
        self.addButton.grid(padx=12, pady=(0, 12), row=1, column=1)
        self.label.grid(padx=12, pady=4, columnspan=2)
        self.statusLabel.grid(padx=12, pady=(4,2), columnspan=2)
        self.listCountLabel.grid(padx=12, pady=(2,4), columnspan=2)
        
        self.nameTutorialLabel.grid(padx=12, pady=12, columnspan=2)
        self.nameEntry.grid(padx=12, pady=(0,12), row=1, column=0)
        self.submitButton.grid(padx=12, pady=(0,12), row=1, column=1)

    def addItemToList(self, itemName):
        self.entry.delete(0, END)
        # Search for Item ID via XIVApi and append to List via {'Name': x, 'ID': y} format
        # Also catch errors and report to the statusLabel if there is a problem
        try:
            itemID = XIVApi.SearchIDByName(itemName)
        except:
            self.statusLabel.configure(text='ERROR: ' + itemName + ' not found.')
        else:
            # Add an empty Dict to List to fill with info in the next step
            self.itemList.append({})
            index = (len(self.itemList) - 1)

            self.itemList[index].update({'Name': itemName, 'ID': itemID})

            self.statusLabel.configure(text='Added ' + itemName + '. ID: ' + itemID )

            # Update list count label
            self.itemOrItems = ""
            self.listLength=len(self.itemList)

            if (self.listLength == 1):
                self.itemOrItems = "item"
            else:
                self.itemOrItems = "items"

            self.listCountLabel.configure(text=str(self.listLength) + ' ' + self.itemOrItems + ' in list.')

    def saveEntries(self, itemList, fileName):
        if (len(itemList) == 0):
            self.window.destroy()
        else:
            Files.WriteDictToCSVFile(itemList, fileName)
            # Empty the item list variable to prepare for the next list.
            self.itemList.clear()

            self.window.destroy()

def DrawGUI():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()

    window = RunWindow(root)
    root.title('XIV MB Tool')
    root.resizable(False,False)
    root.mainloop()
