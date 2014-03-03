'''
Created on Feb 16, 2014

@author: Aaron "Freshman" Wang
'''


from Tkinter import Tk, RIGHT, BOTH, RAISED, NONE
from ttk import Frame, Button, Style
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
        
        ranking = BackEnd.DataHandler.getRanking("TEST")
        
        
        
def Team_Ranking():
    root_team_ranking = Tk()
    root_team_ranking.geometry = ("900x900 +300+300")
    app = TeamRanking(root_team_ranking)
    root_team_ranking.wait_visibility()
    root_team_ranking.mainloop()
    
if __name__ == "__main__":
    Team_Ranking()