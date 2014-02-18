'''
Created on Feb 17, 2014

@author: Aaron "Freshman" Wang
'''
from Tkinter import *
from ttk import Frame, Button, Style

class TeamLookup(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Team Lookup")
        self.style = Style()
        self.style.theme_use("default")
    
def Team_Lookup():
    root_team_lookup = Tk()
    root_team_lookup.geometry("750x650+300+300")
    app_team_lookup = TeamLookup(root_team_lookup)
    root_team_lookup.mainloop()
    
