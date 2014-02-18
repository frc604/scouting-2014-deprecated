'''
Created on Feb 17, 2014

@author: Aaron "Freshman" Wang
'''
from Tkinter import *
from ttk import *

class DataPopulation(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Data Population")
        self.style = Style()
        self.style.theme_use("default")
        
        TeamNumberLabel=Label(self.parent, text="Team Number")
        TeamNumberLabel.pack()
        
        TeamNumberEntry = Entry(self.parent)
        TeamNumberEntry.pack()

def Data_Population():
    root_data_population = Tk()
    root_data_population.geometry("750x650+300+300")
    app_data_population = DataPopulation(root_data_population)
    root_data_population.mainloop()
    
if __name__ == "__main__":
    Data_Population()