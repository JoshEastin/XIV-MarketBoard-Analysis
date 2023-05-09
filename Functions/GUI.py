import customtkinter
from customtkinter import *
import Functions.Files as Files
import Functions.XIVApi as XIVApi
import Functions.Universalis as Universalis
import Functions.Main as Main

worldList = ['Balmung','Behemoth','Brynhildr','Cactuar','Coeurl','Diabolos','Excalibur','Exodus','Faerie','Famfrit','Gilgamesh','Goblin','Halicarnassus','Hyperion','Jenova','Lamia','Leviathan','Maduin','Malboro','Marilith','Mateus','Midgardsormr','Sargatanas','Seraph','Siren','Ultros','Zalera']
filesList = Files.GenerateListOfCSVFiles()

def DrawGUI():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()
    root.geometry('500x350')

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    label = customtkinter.CTkLabel(master=frame, text="XIV Market Volume")
    label.pack(pady=12, padx=10)

    world = StringVar()
    dropdown = customtkinter.CTkOptionMenu(master=frame, variable=world, values=worldList)
    dropdown.pack(pady=12)

    item = StringVar()
    dropdown2 = customtkinter.CTkOptionMenu(master=frame, variable=item, values=filesList)
    dropdown2.pack(pady=12)

    progressLabel = customtkinter.CTkLabel(master=frame, text='')

    button = customtkinter.CTkButton(master=frame, text="Run", command=lambda: Main.main(world.get(), item.get()))
    button.pack(pady=12)

    root.mainloop()
