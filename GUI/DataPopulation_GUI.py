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
        #Team Number
        TeamNumberLabel = Label(self.parent, 
                                text="Team Number")
        TeamNumberLabel.pack()
        TeamNumberEntry = Entry(self.parent)
        TeamNumberEntry.pack()
        
        #Match Number
        MatchNumberLabel = Label(self.parent, 
                                 text="Match Number")
        MatchNumberLabel.pack()
        MatchNumberEntry = Entry(self.parent)
        MatchNumberEntry.pack()
        
        #Alliance
        AllianceLabel = Label(self.parent, 
                              text="Alliance (True for blue,False for Red)") 
        AllianceLabel.pack()
        AllianceEntry = Entry(self.parent)
        AllianceEntry.pack()
        
        #Alliance Scores
        BlueAllianceScoreLabel = Label(self.parent, 
                                       text="Blue Alliance Score")
        BlueAllianceScoreLabel.pack()
        BlueAllianceScoreEntry = Entry(self.parent)
        BlueAllianceScoreEntry.pack()
        
        RedAllianceScoreLabel = Label(self.parent, 
                                      text="Red Alliance Score")
        RedAllianceScoreLabel.pack()
        RedAllianceScoreEntry = Entry(self.parent)
        RedAllianceScoreEntry.pack()
        
        #Autonomous
        #Auton Driving
        AutonDrivingLabel = Label(self.parent,
                                  text="Auton Drive Forward")
        AutonDrivingLabel.pack()
        AutonDrivingEntry = Entry(self.parent)
        AutonDrivingEntry.pack()
        
        #Auton Shooting Position(High/Low)
        AutonShootingPosLabel = Label(self.parent,
                                      text="Auton Shooting Goal High(True)/Low(False)")
        AutonShootingPosLabel.pack()
        AutonShootingPosEntry = Entry(self.parent)
        AutonShootingPosEntry.pack()
        
        #Auton Shooting Success/Fail
        AutonShootingSFLabel = Label(self.parent,
                                     text="Auton Shooting Success(True)/Fail(False")
        AutonShootingSFLabel.pack()
        AutonShootingSFEntry = Entry(self.parent)
        AutonShootingSFEntry.pack()
        
        #Auton Shooting Hot/Not
        AutonShootingHNLabel = Label(self.parent,
                                     text="Auton Shooting Hot(True)/Not(False")
        AutonShootingHNLabel.pack()
        AutonShootingHNEntry = Entry(self.parent)
        AutonShootingHNEntry.pack()
        
        #Teleop
        #Assist Number
        TeleopAssistNumberLabel = Label(self.parent,
                                        text="Number of Assists")
        TeleopAssistNumberLabel.pack()
        TeleopAssistNumberEntry = Entry(self.parent)
        TeleopAssistNumberEntry.pack()
        
        #Teleop Shooting High
        #Teleop Shooting High Attempted
        TeleopHShotsAttemptedLabel = Label(self.parent,
                                           text="Number of High Shots Attempted")
        TeleopHShotsAttemptedLabel.pack()
        TeleopHShotsAttemptedEntry = Entry(self.parent)
        TeleopHShotsAttemptedEntry.pack()
        
        #Teleop Shooting High Successes
        TeleopHShotsMadeLabel = Label(self.parent,
                                      text="Number of High Shots Made")
        TeleopHShotsMadeLabel.pack()
        TeleopHShotsMadeEntry = Entry(self.parent)
        TeleopHShotsMadeEntry.pack()
        
        #Teleop Shooting Low
        #Teleop Shooting Low Attempted
        TeleopLShotsAttemptedLabel = Label(self.parent,
                                           text="Number of Low Shots Attempted")
        TeleopLShotsAttemptedLabel.pack()
        TeleopLShotsAttemptedEntry = Entry(self.parent)
        TeleopLShotsAttemptedEntry.pack()
        
        #Teleop Shooting Low Successes
        TeleopLShotsMadeLabel = Label(self.parent,
                                      text="Number of Low Shots Made")
        TeleopLShotsMadeLabel.pack()
        TeleopLShotsMadeEntry = Entry(self.parent)
        TeleopLShotsMadeEntry.pack()
        
        #Teleop Truss
        #Teleop Truss Attempt Number
        TeleopTrussAttemptedLabel = Label(self.parent,
                                           text="Number of Truss Attempts")
        TeleopTrussAttemptedLabel.pack()
        TeleopTrussAttemptedEntry = Entry(self.parent)
        TeleopTrussAttemptedEntry.pack()
        
        #Teleop Truss Made
        TeleopTrussMadeLabel = Label(self.parent,
                                      text="Number of Truss Successes")
        TeleopTrussMadeLabel.pack()
        TeleopTrussMadeEntry = Entry(self.parent)
        TeleopTrussMadeEntry.pack()
        
        #Teleop Catches Attempted
        TeleopCatchesAttemptedLabel = Label(self.parent,
                                           text="Number of Catches Attempted")
        TeleopCatchesAttemptedLabel.pack()
        TeleopCatchesAttemptedEntry = Entry(self.parent)
        TeleopCatchesAttemptedEntry.pack()
        
        #Teleop Catches Made
        TeleopCatchesMadeLabel = Label(self.parent,
                                      text="Number of Catches Made")
        TeleopCatchesMadeLabel.pack()
        TeleopCatchesMadeEntry = Entry(self.parent)
        TeleopCatchesMadeEntry.pack()
        
        #Fouls
        FoulNumberLabel = Label(self.parent,
                                text="Number of Fouls")
        FoulNumberLabel.pack()
        FoulNumberEntry = Entry(self.parent)
        FoulNumberEntry.pack()
        
        #Technical Fouls
        TechFoulNumberLabel = Label(self.parent,
                                    text="Number of Technical Fouls")
        TechFoulNumberLabel.pack()
        TechFoulNumberEntry = Entry(self.parent)
        TechFoulNumberEntry.pack()
def Data_Population():
    root_data_population = Tk()
    root_data_population.geometry("750x650+300+300")
    app_data_population = DataPopulation(root_data_population)
    root_data_population.mainloop()
    
if __name__ == "__main__":
    Data_Population()