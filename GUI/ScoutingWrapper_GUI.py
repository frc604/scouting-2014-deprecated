'''
Created on Feb 16, 2014

@author: Aaron "Freshman" Wang
'''
from Tkinter import Tk, RIGHT, BOTH, RAISED, NONE
from ttk import Frame, Button, Style
from DataPopulation_GUI import Data_Population
from TeamRanking_GUI import Team_Ranking
import tkMessageBox

class ScoutingWrapper(Frame):
    def __init__(self, parent):
        Frame.__init__(self, 
                       parent)
        
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        
        self.parent.title("Team 604 Scouting App - ver. 0.2")
        
        self.style = Style()
        self.style.theme_use("default")
        
        
        
        frame1 = Frame(self, 
                       relief=RAISED, 
                       borderwidth=1)
        frame1.pack(fill=NONE,
                    expand=1)
        
        #Key Functions
        
        dataPopulationButton = Button(self, 
                                      te1xt="Data Population",
                                      command=Data_Population, 
                                      width=12)   
        dataPopulationButton.pack()
        
        teamLookupButton = Button(self,
                                  text="Export",    # Export module needs to be made 
                                  width=12)           
        teamLookupButton.pack()
        
        teamRankingButton = Button(self, 
                                   text="Team Ranking",
                                   command=Team_Ranking,  
                                   width=12)         
        teamRankingButton.pack()
        
        teamEntryDeletionButton = Button(self,
                                         text="Match Deletion",
                                         width=12)    #TODO: Make TeamEntryDeletion GUI
        teamEntryDeletionButton.pack()
        #Formatting to look pretty

        frame2 = Frame(self, 
                       relief=RAISED, 
                       borderwidth=1)
        frame2.pack(fill=NONE, 
                    expand =1)
        
        
        quitButton = Button(self,
                            text="Quit", 
                            command=self.quit)
        quitButton.pack(side=RIGHT, 
                        padx=15, 
                        pady=5)             #TODO: Fix Button placement  

        self.pack(fill=BOTH, 
                  expand=1)
    def Export_Message_Confirmation():
        
        
def main():

    root_wrapper = Tk()
    root_wrapper.geometry("300x150+300+300")
    app_wrapper = ScoutingWrapper(root_wrapper)
    root_wrapper.mainloop()
    
if __name__ == "__main__":
    main()