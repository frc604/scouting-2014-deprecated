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
        
        aggregated_ranking_list = BackEnd.DataHandler.getRanking("CASJ")
        cycle_ranking_list = aggregated_ranking_list[0]
        assist_ranking_list = aggregated_ranking_list[1]
        truss_ranking_list = aggregated_ranking_list[2]
        shooting_ranking_list = aggregated_ranking_list[3]
#        print aggregated_ranking_list
        catches_ranking_list = aggregated_ranking_list[4]
        
        team_cycle_ranking = []
        lb_cycle_ranking = Listbox(self.parent)
        
        for enum, i in enumerate(cycle_ranking_list):
            print i
            team_cycle_ranking.append(cycle_ranking_list[enum][1])
            lb_cycle_ranking.insert(END,team_cycle_ranking[enum])
        lb_cycle_ranking.pack(side=LEFT, 
                              padx=15, 
                              pady=5)
        
        team_assist_ranking = []
        lb_assist_ranking = Listbox(self.parent)
        
        for enum, j in enumerate(assist_ranking_list):
            team_assist_ranking.append(assist_ranking_list[enum][1])
            lb_assist_ranking.insert(END,team_assist_ranking[enum])
        lb_assist_ranking.pack(side=LEFT,
                               padx=15,
                               pady=5)
            
        team_truss_ranking = []
        lb_truss_ranking = Listbox(self.parent)
        
        for enum, k in enumerate(truss_ranking_list):
            team_truss_ranking.append(truss_ranking_list[enum][1])
            lb_truss_ranking.insert(END,team_truss_ranking[enum])
        lb_truss_ranking.pack(side=LEFT,
                              padx=15,
                              pady=5)
        
        team_shooting_ranking = []
        lb_shooting_ranking = Listbox(self.parent)
        
        for enum, l in enumerate(shooting_ranking_list):
            team_shooting_ranking.append(shooting_ranking_list[enum][1])
            lb_shooting_ranking.insert(END,team_shooting_ranking[enum])
        lb_shooting_ranking.pack(side=LEFT,
                                 padx=15,
                                 pady=5)
        
        team_catches_ranking = []
        lb_catches_ranking = Listbox(self.parent)
        
        for enum, m in enumerate(catches_ranking_list):
            team_catches_ranking.append(catches_ranking_list[enum][1])
            lb_catches_ranking.insert(END,team_catches_ranking[enum])
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