'''
Created on Feb 24, 2014

@author: Aaron "Freshman" Wang
'''
from Tkinter import *
from ttk import *
import BackEnd.DataHandler

class MatchDeletion(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Match Deletion")
        self.Style = Style()
        self.Style.theme_use("default")
        
        TeamNumberDeletionLabel = Label(self.parent, 
                                        text="Team Number")
        TeamNumberDeletionLabel.grid(row=1,column=1)
        
        TeamNumberDeletionEntry = Entry(self.parent)
        TeamNumberDeletionEntry.grid(row=2,column=1)
        
        MatchNumberDeletionLabel = Label(self.parent,
                                         text="Match Number")
        MatchNumberDeletionLabel.grid(row=3,column=1)
        MatchNumberDeletionEntry = Entry(self.parent) 
        MatchNumberDeletionEntry.grid(row=4,column=1)
        
        DeletionButton = Button(self.parent,
                                text="Delete Entry",
                                #command=self.Delete_Data_Aggregation(TeamNumberDeletionEntry, MatchNumberDeletionEntry)
                                )
        DeletionButton.grid(row=6,column=1)
        
        CloseButton = Button(self.parent,
                             text="Close",
                             command=self.parent.quit)
        
        CloseButton.grid(row=6, column=2)
        
    def Delete_Data_Aggregation(self, TeamNumberDeletionEntry, MatchNumberDeletionEntry):
        TeamNumberDeletion = TeamNumberDeletionEntry.get()
        MatchNumberDeletion = MatchNumberDeletionEntry.get()
        
        BackEnd.DataHandler.delete(TeamNumberDeletion,MatchNumberDeletion,"TEST")     #Change this default value.
        
def Match_Deletion():
    root_match_deletion = Tk()
    root_match_deletion.geometry = ("750x750+300+300")
    app = MatchDeletion(root_match_deletion)
    root_match_deletion.mainloop()
    
if __name__ == "__main__":
    Match_Deletion()