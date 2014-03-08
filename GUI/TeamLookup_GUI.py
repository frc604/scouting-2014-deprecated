'''
Created on Feb 17, 2014

@author: Aaron "Freshman" Wang
'''
from Tkinter import *
from ttk import *
import BackEnd.DataHandler

class TeamLookup(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Team Lookup")
        self.style = Style()
        self.style.theme_use("default")
        
        match_performance_history =  BackEnd.DataHandler.getTeam()
        
        shooting_performance_list = match_performance_history["shooting"]
        shooting_performance_h_list = shooting_performance_list[1]
        
        
        assist_performance_list = match_performance_history["assist"]
        
        truss_performance_list = match_performance_history["truss"]
        
        auton_performance_list = match_performance_history["auton"]
        
def Team_Lookup():
    root_team_lookup = Tk()
    root_team_lookup.geometry("750x650+300+300")
    app_team_lookup = TeamLookup(root_team_lookup)
    root_team_lookup.mainloop()
    
if __name__ == "__main__":
    Team_Lookup()