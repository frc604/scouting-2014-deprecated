'''
Created on Feb 17, 2014

@author: Aaron "Freshman" Wang
'''
from Tkinter import *
from ttk import *
import tkMessageBox

class DataPopulation(Frame):
    def __init__(self,parent):
        
        Frame.__init__(self,
                       parent)
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        
        self.parent.title("Data Population")
        self.style = Style()
        self.style.theme_use("default")
        
        #General Info
        #TODO: Label General Info
        
        #Team Number
        TeamNumberLabel = Label(self.parent, 
                                text="Team Number")
        TeamNumberLabel.grid(row=1,column=1)
        TeamNumberEntry = Entry(self.parent)
        TeamNumberEntry.grid(row=2,column=1)
        
        #Match Number
        MatchNumberLabel = Label(self.parent, 
                                 text="Match Number")
        MatchNumberLabel.grid(row=1,column=2)
        MatchNumberEntry = Entry(self.parent)
        MatchNumberEntry.grid(row=2,column=2)
        
        #Alliance
        AllianceLabel = Label(self.parent, 
                              text="Alliance(True for b,False for r)") 
        AllianceLabel.grid(row=1, column=3)
        AllianceEntry = Entry(self.parent)
        AllianceEntry.grid(row=2, column=3)


        #Alliance Scores
        BlueAllianceScoreLabel = Label(self.parent, 
                                       text="Blue Alliance Score")
        BlueAllianceScoreLabel.grid(row=3, column=1)
        BlueAllianceScoreEntry = Entry(self.parent)
        BlueAllianceScoreEntry.grid(row=4, column=1)
        
        RedAllianceScoreLabel = Label(self.parent, 
                                      text="Red Alliance Score")
        RedAllianceScoreLabel.grid(row=3, column=2)
        RedAllianceScoreEntry = Entry(self.parent)
        RedAllianceScoreEntry.grid(row=4, column=2)
        
        #Autonomous
        #TODO: Separate and label the Auton fields
        
        #Auton Driving
        AutonDrivingLabel = Label(self.parent,
                                  text="Auton Drive Forward")
        AutonDrivingLabel.grid(row=5, column=1)
        AutonDrivingEntry = Entry(self.parent)
        AutonDrivingEntry.grid(row=6, column=1)
        
        #Auton Shooting Position(High/Low)
        AutonShootingPosLabel = Label(self.parent,
                                      text="Auton Shooting Goal True/False")     #True being High and False being Low
        AutonShootingPosLabel.grid(row=5, column=2)
        AutonShootingPosEntry = Entry(self.parent)
        AutonShootingPosEntry.grid(row=6, column=2)
        
        #Auton Shooting Success/Fail
        AutonShootingSFLabel = Label(self.parent,
                                     text="Auton Shooting SF True/False")    #True being Success and False being Fail
        AutonShootingSFLabel.grid(row=5, column=3)
        AutonShootingSFEntry = Entry(self.parent)
        AutonShootingSFEntry.grid(row=6, column=3)
        
        #Auton Shooting Hot/Not
        AutonShootingHNLabel = Label(self.parent,
                                     text="Auton Shooting HN True/False")    #True being Hot, False being Not
        AutonShootingHNLabel.grid(row=5, column=4)
        AutonShootingHNEntry = Entry(self.parent)
        AutonShootingHNEntry.grid(row=6, column=4)
                
        #Teleop
        #TODO: Separate and Label the Teleop secion
        #Assist Number
        TeleopAssistNumberLabel = Label(self.parent,
                                        text="Number of Assists")
        TeleopAssistNumberLabel.grid(row=7, column=1)
        TeleopAssistNumberEntry = Entry(self.parent)
        TeleopAssistNumberEntry.grid(row=8, column=1)
        
        #Teleop Shooting High
        #Teleop Shooting High Attempted
        TeleopHShotsAttemptedLabel = Label(self.parent,
                                           text="Number of High Shots Attempted")
        TeleopHShotsAttemptedLabel.grid(row=9, column=1)
        TeleopHShotsAttemptedEntry = Entry(self.parent)
        TeleopHShotsAttemptedEntry.grid(row=10, column=1)
        
        #Teleop Shooting High Successes
        TeleopHShotsMadeLabel = Label(self.parent,
                                      text="Number of High Shots Made")
        TeleopHShotsMadeLabel.grid(row=9, column=2)
        TeleopHShotsMadeEntry = Entry(self.parent)
        TeleopHShotsMadeEntry.grid(row=10, column=2)
        
        #Teleop Shooting Low
        #Teleop Shooting Low Attempted
        TeleopLShotsAttemptedLabel = Label(self.parent,
                                           text="Number of Low Shots Attempted")
        TeleopLShotsAttemptedLabel.grid(row=11, column=1)
        TeleopLShotsAttemptedEntry = Entry(self.parent)
        TeleopLShotsAttemptedEntry.grid(row=12, column=1)
        
        #Teleop Shooting Low Successes
        TeleopLShotsMadeLabel = Label(self.parent,
                                      text="Number of Low Shots Made")
        TeleopLShotsMadeLabel.grid(row=11, column=2)
        TeleopLShotsMadeEntry = Entry(self.parent)
        TeleopLShotsMadeEntry.grid(row=12, column=2)
        
        #Teleop Truss
        #Teleop Truss Attempt Number
        TeleopTrussAttemptedLabel = Label(self.parent,
                                           text="Number of Truss Attempts")
        TeleopTrussAttemptedLabel.grid(row=13, column=1)
        TeleopTrussAttemptedEntry = Entry(self.parent)
        TeleopTrussAttemptedEntry.grid(row=14, column=1)
        
        #Teleop Truss Made
        TeleopTrussMadeLabel = Label(self.parent,
                                      text="Number of Truss Successes")
        TeleopTrussMadeLabel.grid(row=13, column=2)
        TeleopTrussMadeEntry = Entry(self.parent)
        TeleopTrussMadeEntry.grid(row=14, column=2)
        
        #Catches
        #Teleop Catches Attempted
        TeleopCatchesAttemptedLabel = Label(self.parent,
                                           text="Number of Catches Attempted")
        TeleopCatchesAttemptedLabel.grid(row=15, column=1)
        TeleopCatchesAttemptedEntry = Entry(self.parent)
        TeleopCatchesAttemptedEntry.grid(row=16, column=1)
        
        #Teleop Catches Made
        TeleopCatchesMadeLabel = Label(self.parent,
                                      text="Number of Catches Made")
        TeleopCatchesMadeLabel.grid(row=15, column=2)
        TeleopCatchesMadeEntry = Entry(self.parent)
        TeleopCatchesMadeEntry.grid(row=16, column=2)
        
        #Separate and Label Fouls section
        #Fouls
        FoulNumberLabel = Label(self.parent,
                                text="Fouls")
        FoulNumberLabel.grid(row=17, column=1)
        FoulNumberEntry = Entry(self.parent)
        FoulNumberEntry.grid(row=18, column=1)
        
        #Technical Fouls
        TechFoulNumberLabel = Label(self.parent,
                                    text="Technical Fouls")
        TechFoulNumberLabel.grid(row=17, column=2)
        TechFoulNumberEntry = Entry(self.parent)
        TechFoulNumberEntry.grid(row=18, column=2)
        
        #Alliance Fouls
        AllianceFoulNumberLabel = Label(self.parent,
                                        text="Alliance Fouls")
        AllianceFoulNumberLabel.grid(row=17,column=3)
        AllianceFoulNumberEntry = Entry(self.parent)
        AllianceFoulNumberEntry.grid(row=18,column=3)
        
        #Cards
        CardNumberLabel = Label(self.parent,
                                text="Cards")
        CardNumberLabel.grid(row=17, column=4)
        CardNumberEntry = Entry(self.parent)
        CardNumberEntry.grid(row=18, column=4)
        
def Data_Population():
    root_data_population = Tk()
    root_data_population.geometry("850x850+300+300")
    app_data_population = DataPopulation(root_data_population)
    root_data_population.mainloop()
    
if __name__ == "__main__":
    Data_Population()