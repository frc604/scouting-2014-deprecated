'''
Created on Feb 17, 2014

@author: Alan "LizardPuppy" Li
'''

"""Data files are stored in ./Data/Raw/ as files with the naming format:
<reigonal name>_<team number>_<match number>.604
for match data and
<reigonal name>_<team number>__index.604
for the match index"""

import pickle

def _input(_in):
    """Takes a dictionary _in with the keys:
    team: int- team number
    match: int- match number
    reigonal: string- name of reigonal
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
    
    with open('./Data/Raw/'+_in['reigonal']+'_'+str(_in['team'])+'_'+str(_in['match'])+'.604', 'wb') as _file:
        pickle.dump(_in, _file)
    with open('./Data/Raw/'+_in['reigonal']+'_'+str(_in['team'])+'__index'+'.604', 'rb') as _file:
        matches_played = pickle.load(_file)
    with open('./Data/Raw/'+_in['reigonal']+'_'+str(_in['team'])+'__index'+'.604', 'wb') as _file:
        pickle.dump(matches_played+[_in['match']], _file)
    #TODO: write to the actual SQL database (or be lazy and just use this)
        
def delete(team, match, reigonal):
    """Deletes data for a team, match, and reigonal if you screwed up"""

def getMatchHistory(team, reigonal):
    """Takes in a team number and reigonal name (string) and spits a list of the dictionaries
    detailed above back out at you"""
    
    match_data=[]
    with open('./Data/Raw/'+reigonal+'_'+str(team)+'__index.604', 'rb') as _file:
        matches_played = pickle.load(_file)
    for match in matches_played:
        with open('./Data/Raw/'+reigonal+'_'+str(team)+'_'+str(match)+'.604', 'rb') as _file:
            match_data += [pickle.load(_file)]
    return match_data
    
def getTeam(team, reigonal):
    """Takes in a team number and reigonal name and spits out a dictionary with the keys:
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
def getRanking(reigonal):
    """For a given reigonal name, outputs a huge list of lists of the form:
    [team number, median succesful shots on high goal, medan assists, power rating]"""
