'''
Created on Feb 17, 2014

@author: Alan "LizardPuppy" Li
'''
def _input(_in):
    """Takes a dictionary _in with the keys:
    team: int- team number
    match: int- match number
    alliance: boolean- True for blue, False for red
    score: list- [blue score, red score]
    auton: list-
        [driving, shooting]
        driving: boolean- True for success, False for fail
        shooting: list-
            [position, success, hot]
            position: boolean- True for high, False for low
            success: boolean- True/False
            hot: boolean- True/False
    teleop: dictionary
        assists: int- number of assists
        shots: list-
            [high, low]
            high: list- [shots attempted, shots fired]
            low: list- [shots attempted, shots fired]
        truss: list- [attempts, successes]
        catch: int- catch number
        fouls: list-
            [foul, technical, alliance, cards]
            foul: int- normal fouls
            technical: int- technical fouls
            alliance: int- alliance fouls
            cards: int- yellow cards
        cycles: int- number of cycles
        comments: string- additional comments"""
def getMatchHistory(number):
    """Takes in a team number and spits a list of the dictionaries
    detailed above back out at you"""
def getTeam(number):
    """Takes in a team number and spits out a dictionary with the keys:
    shooting: list of floats-
        [[median succesful shots on high goal, standard deviation],
        [median succesful shots on low goal, standard deviation],
        shooting success percentage]        
    assist: list of floats-
        [median assists, median cycle time]
    truss: list of floats-
        [median truss successes, standard deviation, success percentage]
    power: float- power rating thing
    """
def getRanking():
    """Outputs a huge list of lists of the form:
    [team number, median succesful shots on high goal, medan assists, power rating]"""