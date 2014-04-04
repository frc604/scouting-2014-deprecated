'''
Created on Feb 17, 2014

@author: Alan "LizardPuppy" Li
'''

"""Data files are stored in ../BackEnd/Data/Raw/ as files with the naming format:
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
            high: list- [shots attempted, successes]
            low: list- [shots attempted, successes]
        truss: list- [attempts, successes]
        catch: list- [attempts, successes]
        fouls: list-
            [foul, technical, alliance, cards]
            foul: int- normal fouls
            technical: int- technical fouls
            alliance: int- alliance fouls
            cards: int- yellow cards
        cycles: int- number of cycles
        strategy: string- defense, shooting, not doing jack, etc.
        comments: string- additional comments"""
    try:
        os.makedirs('../BackEnd/Data/Raw/')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    try:
        with open('../BackEnd/Data/Raw/'+_in['regional']+'_team_index.604', 'rb') as _file:
            teams_in_reigonal = pickle.load(_file)
    except IOError:
        teams_in_reigonal = []
    teams_in_reigonal=list(set(teams_in_reigonal+[_in['team']]))
    with open('../BackEnd/Data/Raw/'+_in['regional']+'_team_index.604', 'wb') as _file:
        pickle.dump(teams_in_reigonal,_file)
    with open('../BackEnd/Data/Raw/'+_in['regional']+'_'+str(_in['team'])+'_'+str(_in['match'])+'.604', 'wb') as _file:
        pickle.dump(_in, _file)
    try:
        with open('../BackEnd/Data/Raw/'+_in['regional']+'_'+str(_in['team'])+'__index.604', 'rb') as _file:
            matches_played = pickle.load(_file)
    except IOError:
        matches_played = []
    with open('../BackEnd/Data/Raw/'+_in['regional']+'_'+str(_in['team'])+'__index.604', 'wb') as _file:
        pickle.dump(list(set(matches_played+[_in['match']])), _file)
        
def delete(team, match, regional):
    """Deletes data for a team, match, and regional if you screwed up. Returns 1 if it works and 0 if it didn't (no file found)."""
    try:
        os.remove('../BackEnd/Data/Raw/'+regional+'_'+str(team)+'_'+str(match)+'.604')
    except:
        return 0
    with open('../BackEnd/Data/Raw/'+regional+'_'+str(team)+'__index.604', 'rb') as _file:
        matches_played = pickle.load(_file)
    matches_played.remove(match)
    with open('../BackEnd/Data/Raw/'+regional+'_'+str(team)+'__index.604', 'wb') as _file:
        pickle.dump(matches_played, _file)
    return 1

def getMatchHistory(team, regional):
    """Takes in a team number and regional name (string) and spits a list of the dictionaries
    detailed above back out at you, returns and empty list if there are no matches."""
    match_data=[]
    try:
        with open('../BackEnd/Data/Raw/'+regional+'_'+str(team)+'__index.604', 'rb') as _file:
            matches_played = pickle.load(_file)
    except:
        return match_data
    for match in matches_played:
        with open('../BackEnd/Data/Raw/'+regional+'_'+str(team)+'_'+str(match)+'.604', 'rb') as _file:
            match_data += [pickle.load(_file)]
    return match_data
    
def getTeam(team, regional):
    """Takes in a team number and regional name and spits out a dictionary with the keys:
    shooting: list of floats-
        [[median attempted shots on high goal*shooting success percentage, standard deviation for succesful shots],
        [median attempted shots on low goal*shooting success percentage, standard deviation for succesful shots],
        [shooting success percentage for high goal, shooting success percentage for low goal]]
    assist: list of floats and ints-
        [[median assists, median cycle time],
        [meduan attempted catches*catch success percentage, catch percentage, standard deviation for succesful catches]]
    truss: list of floats-
        [median attempted truss shots*success percentage, standard deviation, success percentage]
    auton: list of floats-
        [success percentage for shooting, ratio of hot goal shots to not hot goal shots, ratio of high goal shots to low goal shots,
        success percentage for driving]


    Additional note - all percentages are decimals (less than 1)
    """
    match_data=getMatchHistory(team, regional)
    result={}
    result['shooting']=[[0,0],[0,0],[[0,0],[0,0]]]
    shooting_data = getGoals(match_data)
    assist_data = getAssists(match_data)
    truss_data = getTruss(match_data)
    auton_data = getAuton(match_data)

    shooting_successes_h=[]
    shooting_attempts_h=[]
    shooting_totals_h=[0,0]
    shooting_successes_l=[]
    shooting_attempts_l=[]
    shooting_totals_l=[0,0]

    for element in shooting_data[0]:
        shooting_attempts_h+=[element[0]]
        shooting_totals_h[0]+=element[0]
        shooting_successes_h+=[element[1]]
        shooting_totals_h[1]+=element[1]
    for element in shooting_data[1]:
        shooting_attempts_l+=[element[0]]
        shooting_totals_l[0]+=element[0]
        shooting_successes_l+=[element[1]]
        shooting_totals_l[1]+=element[1]
    result['shooting'][2][0]=findP(shooting_totals_h[0],shooting_totals_h[1],0,1,0,.000001)
    result['shooting'][2][1]=findP(shooting_totals_l[0],shooting_totals_l[1],0,1,0,.000001)
    result['shooting'][0][0]=median(shooting_attempts_h)*result['shooting'][2][0]
    result['shooting'][1][0]=median(shooting_attempts_l)*result['shooting'][2][1]
    result['shooting'][0][1]=std(shooting_successes_h)
    result['shooting'][1][1]=std(shooting_successes_l)

    assisting=getAssists(match_data)
    assists=assisting[0]
    cycles=assisting[1]
    cycle_time=[]
    catch_attempts=assisting[2][0]
    catch_successes=assisting[2][1]
    catch_attempt_sum=0
    catch_success_sum=0
    for element in assisting[2][0]:
        catch_attempt_sum+=element
    for element in assisting[2][1]:
        catch_success_sum+=element
    for element in cycles:
        cycle_time+=[140/element]
    result['assists'] = [[0,0],[0,0,0]]
    result['assists'][0][0]=median(assists)
    result['assists'][0][1]=median(cycle_time)
    result['assists'][1][1]=findP(catch_attempt_sum,catch_success_sum,0,1,0,.000001)
    result['assists'][1][0]=median(catch_attempts)*result['assists'][1][1]
    result['assists'][1][2]=std(catch_successes)

    truss=getTruss(match_data)
    truss_attempts=0
    truss_success=0
    for element in truss[0]:
        truss_attempts+=element
    for element in truss[1]:
        truss_success+=element
    result['truss'] = [0,0,0]
    result['truss'][2]=findP(truss_attempts,truss_success,0,1,0,.000001)
    result['truss'][0]=median(truss_attempts)*result['truss'][2]
    result['truss'][1]=std(truss_success)

    auton=getAuton(match_data)
    if not auton: # fixme hack
        auton = [0,0,0,0,0]
    result['auton'] = [0,0,0,0]
    result['auton'][0]=findP(auton[0],auton[3],0,1,0,.000001)
    result['auton'][1]=findP(auton[0],auton[4],0,1,0,.000001)
    result['auton'][2]=findP(auton[0],auton[2],0,1,0,.000001)
    result['auton'][3]=findP(auton[0],auton[1],0,1,0,.000001)
    return result
    
def getRanking(regional):
    """For a given regional name, outputs a huge list of lists of the form:
    [[[team number, median cycle time],...]
    [[team number, median assists number],...]
    [[team number, median truss number],...]
    [[team number, median attempted shots on high goal*shooting success percentage],...]
    [[team number, median catches],...]]    

    It's sorted already
    """
    try:
        with open('../BackEnd/Data/Raw/'+str(regional)+'_team_index.604', 'rb') as _file:
            teams = pickle.load(_file)
    except:
        return []
    out = [[],[],[],[],[]]
    for team in teams:
        data=getTeam(team, regional)
        out[0]+=[[team,data['assists'][0][1]]]
        out[1]+=[[team,data['assists'][0][0]]]
        out[2]+=[[team,data['truss'][0]]]
        out[3]+=[[team,data['shooting'][0][0]]]
        out[4]+=[[team,data['assists'][1][0]]]
    out[0].sort(key=lambda x: x[1], reverse=False)
    out[1].sort(key=lambda x: x[1], reverse=True)
    out[2].sort(key=lambda x: x[1], reverse=True)
    out[3].sort(key=lambda x: x[1], reverse=True)
    out[4].sort(key=lambda x: x[1], reverse=True)
    return out

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
        out[2][1]+=[element['teleop']['catch'][0]]
        out[2][1]+=[element['teleop']['catch'][1]]
    return out

def getTruss(data):
    out=[[],[]]
    for element in data:
        out[0]+=[element['teleop']['truss'][0]]
        out[1]+=[element['teleop']['truss'][1]]
    return out

def getAuton(data):
    """[matches, driving successes, high, success, hot]"""
    out=[0,0,0,0,0]
    for element in data:
        out[0]+=1
        if element['auton'][0]:
            out[1]+=1
        if element['auton'][1][0]:
            out[2]+=1
        if element['auton'][1][1]:
            out[3]+=1
        if element['auton'][1][2]:
            out[4]+=1
        
    
#def calcPower(data):

def calcSuccesses(data):
    """data is of form [[list of attempts], [list of succeses]], outputs [adjusted succeses, standard deviation, success percentage]"""
    attempts=0
    succeses=0
    for element in data[0]:
        attempts+=element
    for element in data[1]:
        succeses+=element
    percentage=findP(attempts, succeses, 1, 0, 0.000001)
    return([median(data[0])*percentage, std(data[1]), percentage])

def findP(n, q, nCq, upper, lower, tolerance):
    """binary seraches for p using the following formula:
    (nCq) * integral from p to 0 of (t^q)(1-t)^(n-q) dt = 1/2 """
    if (nCq==0):
        print n
        print q
        nCq=float(comb(n, q, exact=True))
        print nCq
    if nCq == 0:
        return 0
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


def importData(path, regional):
    """Takes a path and a regional name and imports the data at that path"""
    try:
        with open(path+str(regional)+'_team_index.604', 'rb') as _file:
            teams_import = pickle.load(_file)
    except:
        return
    
    try:
        with open('../BackEnd/Data/Raw/'+_in['regional']+'_team_index.604', 'rb') as _file:
            teams_in_reigonal = pickle.load(_file)
    except IOError:
        teams_in_reigonal = []

    for team in teams_import:
        teams_in_reigonal=list(set(teams_in_reigonal+[team]))
        try:
            with open(path+regional+'_'+str(team)+'__index.604', 'rb') as _file:
                matches_import = pickle.load(_file)
        except IOError:
            matches_import = []
        for match in matches_import:
            with open(path+regional+'_'+str(team)+'_'+str(match)+'.604', 'rb') as _file:
                _input(pickle.load(_file))
    with open('../BackEnd/Data/Raw/'+_in['regional']+'_team_index.604', 'wb') as _file:
        pickle.dump(teams_in_reigonal,_file)

def export(path, regional):
    """Takes a path (with slash at end) and exports to that path. Filename will be scouting.xls """
    out = xlwt.Workbook()
    try:
        with open('../BackEnd/Data/Raw/'+str(regional)+'_team_index.604', 'rb') as _file:
            teams = pickle.load(_file)'
    except:
        return
    for team in teams:
        sheet=out.add_sheet(str(team))
        sheet.write(0,0,'Team number')
        sheet.write(0,1,str(team))
        sheet.write(1,4,'Auton')
        sheet.write(1,8,'Teleop')
        sheet.write(1,18,'Penalties')
        sheet.write(2,0,'Match #')
        sheet.write(2,1,'Alliance')
        sheet.write(2,2,'Blue Score')
        sheet.write(2,3,'Red Score')
        sheet.write(2,4,'Drove')
        sheet.write(2,5,'High Goal Success?')
        sheet.write(2,6,'Low Goal Success?')
        sheet.write(2,7,'Hot goal?')
        sheet.write(2,8,'Strategy')
        sheet.write(2,9,'High Attempts')
        sheet.write(2,10,'High Succeses')
        sheet.write(2,11,'Low Attempts')
        sheet.write(2,12,'Low Succeses')
        sheet.write(2,13,'Cycles')
        sheet.write(2,14,'Truss Attempts')
        sheet.write(2,15,'Truss Succeses')
        sheet.write(2,16,'Catch Attempts')
        sheet.write(2,17,'Catch Successes')
        sheet.write(2,18,'Assist Number')
        sheet.write(2,19,'Foul')
        sheet.write(2,20,'Tech')
        sheet.write(2,21,'Card')
        sheet.write(2,22,'Alliance')
        sheet.write(2,23,'Comments')
        history=getMatchHistory(team, regional)
        index=3
        for match in history:
            sheet.write(index,0,match['match'])
            if match['alliance']:
                sheet.write(index,1,'Blue')
            else:
                sheet.write(index,1,'Red')
            sheet.write(index,2,match['score'][0])
            sheet.write(index,3,match['score'][1])
            sheet.write(index,4,match['auton'][0])
            sheet.write(index,5,match['auton'][1][0]&match['auton'][1][1])
            sheet.write(index,6,(not match['auton'][1][0])&match['auton'][1][1])
            sheet.write(index,7,match['auton'][1][3])
            sheet.write(index,8,match['teleop']['strategy'])
            sheet.write(index,9,match['teleop']['shots'][0][0])
            sheet.write(index,10,match['teleop']['shots'][0][1])
            sheet.write(index,11,match['teleop']['shots'][1][1])
            sheet.write(index,12,match['teleop']['shots'][1][1])
            sheet.write(index,13,match['teleop']['cycles'])
            sheet.write(index,14,match['teleop']['truss'][0])
            sheet.write(index,15,match['teleop']['truss'][1])
            sheet.write(index,16,match['teleop']['catch'][0])
            sheet.write(index,17,match['teleop']['catch'][1])
            sheet.write(index,18,match['teleop']['assists'])
            sheet.write(index,19,match['teleop']['fouls'][0])
            sheet.write(index,20,match['teleop']['fouls'][1])
            sheet.write(index,21,match['teleop']['fouls'][2])
            sheet.write(index,22,match['teleop']['fouls'][3])
            sheet.write(index,23,match['teleop']['comments'])
            index+=1
    out.save(path+'scouting.xls')
