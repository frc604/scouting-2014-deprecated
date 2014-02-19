'''
Created on Feb 17, 2014

@author: Alan "LizardPuppy" Li
'''

"""Data files are stored in ./Data/Raw/ as files with the naming format:
<regional name>_<team number>_<match number>.604
for match data and
<regional name>_<team number>__index.604
for the match index"""

import pickle
import os
import errno
from scipy.misc import comb
from scipy.integrate import quad
from numpy import median
from numpy import std

def _input(_in):
    """Takes a dictionary _in with the keys:
    team: int- team number
    match: int- match number
    regional: string- name of regional
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
        catch: list- [attempts, successes]
        fouls: list-
            [foul, technical, alliance, cards]
            foul: int- normal fouls
            technical: int- technical fouls
            alliance: int- alliance fouls
            cards: int- yellow cards
        cycles: int- number of cycles
        comments: string- additional comments"""
    try:
        os.makedirs('./Data/Raw/')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    with open('./Data/Raw/'+_in['regional']+'_'+str(_in['team'])+'_'+str(_in['match'])+'.604', 'wb') as _file:
        pickle.dump(_in, _file)
    with open('./Data/Raw/'+_in['regional']+'_'+str(_in['team'])+'__index.604', 'rb') as _file:
        matches_played = pickle.load(_file)
    with open('./Data/Raw/'+_in['regional']+'_'+str(_in['team'])+'__index.604', 'wb') as _file:
        pickle.dump(matches_played+[_in['match']], _file)
        
def delete(team, match, regional):
    """Deletes data for a team, match, and regional if you screwed up"""
    
    os.remove('./Data/Raw/'+regional+'_'+str(team)+'_'+str(match)+'.604')
    with open('./Data/Raw/'+regional+'_'+str(team)+'__index.604', 'rb') as _file:
        matches_played = pickle.load(_file)
    matches_played.remove(match)
    with open('./Data/Raw/'+regional+'_'+str(team)+'__index.604', 'wb') as _file:
        pickle.dump(matches_played, _file)

def getMatchHistory(team, regional):
    """Takes in a team number and regional name (string) and spits a list of the dictionaries
    detailed above back out at you"""
    
    match_data=[]
    with open('./Data/Raw/'+regional+'_'+str(team)+'__index.604', 'rb') as _file:
        matches_played = pickle.load(_file)
    for match in matches_played:
        with open('./Data/Raw/'+regional+'_'+str(team)+'_'+str(match)+'.604', 'rb') as _file:
            match_data += [pickle.load(_file)]
    return match_data
    
def getTeam(team, regional):
    """Takes in a team number and regional name and spits out a dictionary with the keys:
    shooting: list of floats-
        [[median attempted shots on high goal*shooting success percentage, standard deviation],
        [median attempted shots on high goal*shooting success percentage, standard deviation],
        [shooting success percentage for high goal, shooting success percentage for low goal]]
    assist: list of floats-
        [[median assists, median cycle time],
        [meduan attempted catches*catch success percentage, catch percentage]]
    truss: list of floats-
        [median attempted truss shots*success percentage, standard deviation, success percentage]
    auton: list of floats-
        [success percentage, ratio of hot goal shots to not hot goal shots, ratio of high goal shots to low goal shots]
    power: float- power rating thing


    Additional note - all percentages are decimals (less than 1)
    """
    match_data=getMatchHistory(team, regional)
    result={}
    
    
def getRanking(regional):
    """For a given regional name, outputs a huge list of lists of the form:
    [team number, median attempted shots on high goal*shooting success percentage,
    meduan attempted catches*catch success percentage, power rating]"""



"""Extra helper functions"""
def getGoals(data):
    """[high goal stuff, low goal stuff]"""
    out=[[],[]]
    for element in data:
        out[0]+=[element['teleop']['shots'][0]]
        out[1]+=[element['teleop']['shots'][1]]
    return out

def getAssists(data):
    """[assists, cycles, [attempted catches, succesful catches]]"""
    out=[[],[],[[],[]]]
    for element in data:
        out[0]+=[element['teleop']['assists']]
        out[1]+=[element['teleop']['cycles']]
        out[3][1]+=[element['teleop']['catch'][0]]
        out[3][1]+=[element['teleop']['catch'][1]]
    return out

def getTruss(data, position):
    out=[[],[]]
    for element in data:
        out[0]+=[element['teleop']['truss'][0]]
        out[1]+=[element['teleop']['truss'][1]]
    return out

def calcPower(data):

def calcSuccesses(data):
    """data is of form [[list of attempts], [list of succeses]], outputs [adjusted succeses, standard deviation, success percentage]"""
    attempts=0
    succeses=0
    for element in data[0]:
        attempts+=element
    for element in data[1]:
        succeses+=element
    percentage=findP(attempts, succeses, 1, 0, 0.000001)
    return([median(data[0])*percentage, std(data[1]), percentage)

def findP(n, q, nCq, upper, lower, tolerance):
    """binary seraches for p using the following formula:
    (nCq) * integral from p to 0 of (t^q)(1-t)^(n-q) dt = 1/2 """
    if (nCq==0):
        nCq=float(comb(n, q, exact=True))
    test=(upper+lower)/2.0
    val=quad(integrand, 0, test, args=(n,q))
    if ((val[0]-1/(2*nCq))<tolerance):
        return val[0]
    elif (val[0]<(1/(2*nCq))):
        return findP(n, q, nCq, upper, test, tolerance)
    else:
        return findP(n, q, nCq, test, lower, tolerance)

def integrand(x, n, q):
    return (x**q)*(1-x)**(n-q)






    
