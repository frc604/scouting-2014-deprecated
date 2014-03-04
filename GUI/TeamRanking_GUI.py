'''
Created on Feb 16, 2014

@author: Aaron "Freshman" Wang
'''


from Tkinter import *
from ttk import *
import BackEnd.DataHandler

class TeamRanking(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self,):
        self.parent.title("Team Ranking")
        self.Style = Style( )
        self.Style.theme_use("default")
        
        aggregated_ranking_list = BackEnd.DataHandler.getRanking("TEST")
        cycle_ranking_list = aggregated_ranking_list[1]
        assist_ranking_list = aggregated_ranking_list[2]
        truss_ranking_list = aggregated_ranking_list[3]
        shooting_ranking_list = aggregated_ranking_list[4]
        catches_ranking_list = aggregated_ranking_list[5]
        
        team_cycle_ranking = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],] #TODO: Change the number of lists in this list per regional.
        
        lb_cycle_ranking = Listbox(self.parent)
        
        for i in cycle_ranking_list:
            team_cycle_ranking[i][1] = cycle_ranking_list[i][1]
            lb_cycle_ranking.INSERT(END,team_cycle_ranking[i][1]) 
        
        
def Team_Ranking():
    root_team_ranking = Tk()
    root_team_ranking.geometry = ("900x900+300+300")
    app = TeamRanking(root_team_ranking)
    root_team_ranking.wait_visibility()
    root_team_ranking.mainloop()
    
if __name__ == "__main__":
    Team_Ranking()