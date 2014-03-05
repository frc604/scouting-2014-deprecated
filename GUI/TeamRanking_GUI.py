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
        
        team_cycle_ranking = []
        lb_cycle_ranking = Listbox(self.parent)
        
        for i in cycle_ranking_list:
            team_cycle_ranking[i] = cycle_ranking_list[i][1]
            lb_cycle_ranking.INSERT(END,team_cycle_ranking[i]) 
        lb_cycle_ranking.pack(side=LEFT, 
                              padx=15, 
                              pady=5)
        
        team_assist_ranking = []
        lb_assist_ranking = Listbox(self.parent)
        
        for j in assist_ranking_list:
            team_assist_ranking[j] = assist_ranking_list[j][1]
            lb_assist_ranking.INSERT(END,team_assist_ranking[j])
        lb_assist_ranking.pack(side=LEFT,
                               padx=15,
                               pady=5)
            
        team_truss_ranking = []
        lb_truss_ranking = Listbox(self.parent)
        
        for k in truss_ranking_list:
            team_truss_ranking[k] = truss_ranking_list[k][1]
            lb_truss_ranking.INSERT(END,team_truss_ranking[k])
        lb_truss_ranking.pack(side=LEFT,
                              padx=15,
                              pady=5)
        
        team_shooting_ranking = []
        lb_shooting_ranking = Listbox(self.parent)
        
        for l in shooting_ranking_list:
            team_shooting_ranking[l] = shooting_ranking_list[l][1]
            lb_shooting_ranking.INSERT(END,team_shooting_ranking[l])
        lb_shooting_ranking.pack(side=LEFT,
                                 padx=15,
                                 pady=5)
        
        team_catches_ranking = []
        lb_catches_ranking = Listbox(self.parent)
        
        for m in catches_ranking_list:
            team_catches_ranking[m] = catches_ranking_list[m][1]
            lb_catches_ranking.INSERT(END,team_catches_ranking[m])
        lb_catches_ranking.pack(side=LEFT,
                                 padx=15,
                                 pady=5)
        
def Team_Ranking():
    root_team_ranking = Tk()
    root_team_ranking.geometry = ("900x900+300+300")
    app = TeamRanking(root_team_ranking)
    root_team_ranking.wait_visibility()
    root_team_ranking.mainloop()
    
if __name__ == "__main__":
    Team_Ranking()