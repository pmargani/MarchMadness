from pprint import pprint
import random
import math
import sys

"""
This is a module for using NCAA head coache's salaries 
for determining the results of March Madness
"""

# Instead of scraping the teams from a web site or using an API,
# it was simpler to simply hardcode them here for 2023 as flat lists,
# where the first two play eachother in the first game, and so.

south = [
    "Alabama",
    "Texas A&M",
    "Maryland",
    "West Virginia",
    "San Diego State",
    "Charleston",
    "Virginia",
    "Furman",
    "Creighton",
    "NC State",
    "Baylor",
    "UC Santa Barbara",
    "Missouri",
    "Utah State",
    "Arizona",
    "Princeton"
]

east = [
    "Purdue",
    "TX Southern",
    "Memphis",
    "Florida Atlantic",
    "Duke",
    "Oral Roberts",
    "Tennessee",
    "Louisiana",
    "Kentucky",
    "Providence",
    "Kansas State",
    "Montana State",
    "Michigan State",
    "USC",
    "Marquette",
    "Vermont"
]

midwest = [
    "Houston",
    "Northern Kentucky",
    "Iowa",
    "Auburn",
    "Miami",
    "Drake",
    "Indiana",
    "Kent State",
    "Iowa State",
    "Mississippi State",
    "Xavier",
    "Kennesaw State",
    "Texas A&M",
    "Penn State",
    "Texas",
    "Colgate"
]

west = [
    "Kansas",
    "Howard",
    "Arkansas",
    "Illinois",
    "Saint Mary's",
    "VCU",
    "UConn",
    "Iona",
    "TCU",
    "Arizona State",
    "Gonzaga",
    "Grand Canyon",
    "Northwestern",
    "Boise State",
    "UCLA",
    "UNC Asheville"
]

salaryChoices = 0
randomChoices = 0  
        
def getCoachesSalaries(filename):
    """
    Parses file which has form:
    coach name\tteam name\t$32,000
    """
    with open(filename, 'r') as f:
        ls = f.readlines()

    d = {}
    for l in ls:
        print(l, l.split("\t"))
        parts = l.split("\t")
        team = parts[1]
        # $32,000\n -> 32000
        salaryStr = parts[2][1:-1]
        salary = int(salaryStr.replace(',', ''))
        d[team] = salary
    return d

def makeBracket(teams):
    "[0,1,2,3] -> [(0,1),(2,3)]"
    b = []
    for i in range(0, len(teams), 2):
        b.append((teams[i], teams[i+1]))
    return b
        

def chooseWinner(teams, salaries):
    """
    For a given tuple of teams playing eachother,
    attempt to determine the winner based off the given
    dictionary of salaries of each team's head coach.
    """
    global salaryChoices
    global randomChoices

    t1, t2 = teams

    # use the average salary if a team doesn't have one
    if t1 not in salaries or t2 not in salaries:
        randomChoices += 1
        avgSalary = sum([v for k, v in salaries.items()]) / len(salaries)
    else:
        salaryChoices += 1

    # get the salaries
    if t1 in salaries:
        t1salary = salaries[t1]
    else:
        t1salary = avgSalary

    if t2 in salaries:
        t2salary = salaries[t2]
    else:
        t2salary = avgSalary

    # use that to determine the winner
    if t1salary > t2salary:
        return t1
    else:
        return t2

def getRegionalBracket(bracket, levels, salaries):
    """"
    Reduce list of paired teams till there's just one winner.
    This uses a recursive algorithm rather then a for loop
    """
    if len(bracket) == 1:
        # this is the terminating sequent
        return chooseWinner(bracket[0], salaries), levels
    else:
        # recurse!  pick a winner   
        winners = []
        for i in range(0, len(bracket), 2):
            winners.append((chooseWinner(bracket[i],salaries), chooseWinner(bracket[i+1], salaries)))
        levels.append(winners)
        # and call this again!
        return getRegionalBracket(winners, levels, salaries)  

def printLevels(name, teams, levels, winner, salaries):
    """
    This prints the results from the getRegionalBracket
    in a way that shows how the bracket progresses, along
    with the salary info that determined each game

    The basic algorithm here is to print the first series of
    games furthest to the left, then the winners of those games
    get printed a little further to the right, in between, and so on.
    """

    numTeams = len(teams)
    numCols = int(math.log2(numTeams))
    numRows = numTeams*2

    # first create a list that will hold tuples of
    # (column to be printed in, team name)
    ls = [None]*numRows

    # first games are just the original flat list
    col = 0
    for i in range(numTeams):
        ls[i*2] = (col, teams[i]) 
   
    # the rest of the games proceed futher to the right
    for col in range(1, numCols):
        start = (2**col)-1 
        step = 2**(col+1)
        numTeams = numTeams // 2
        # make a list from the list of tuples
        colTeams = []
        for a, b in levels[col-1]:
            colTeams.append(a)
            colTeams.append(b)
        # put the teams in their place    
        for i in range(numTeams):
            ls[start + step*i] = (col, colTeams[i])  

    # add winner
    ls[len(teams)-1] = (numCols, winner)

    # now we can actually print the bracket
    print("") 
    print(name)
    colWidth = 15   
    for i, l in enumerate(ls):
        
        if l is not None:
            col, team = l
            s = ""
            if team in salaries:
                s = "($%5.3fM)" % (salaries[team]/1e6)
            else:
                s = "(avg)"    
            print(col*colWidth*" " + team + " " + s)
        else:
            print(" ")    

def predictMarchMadness(fn):
    "Use coaches salaries to determine the winner of March Maddness"

    teams = west + midwest + east + south

    # fn = "/Users/pmargani/Documents/NCAACoachSalaries.txt"
    # fn2 = "/Users/pmargani/Documents/coachSalaries2.txt"

    # parse the given file for salaries
    salaries = getCoachesSalaries(fn)

    # pprint(salaries)
   
    # how well does the salary file cover this year's teams
    bads = 0
    for team in teams:
        if team not in salaries:
            print("team not in salaries: ", team)
            bads += 1

    print("num teams in bracket: ", len(teams))
    print("num teams with salaries: ", len(salaries))
    print("num teams in bracket with no salary: ", bads)     

    # resolve the four different regional brackets 
    # using the salary information
    westBracket = makeBracket(west)
    levels = []
    westWinner, westLevels = getRegionalBracket(westBracket, levels, salaries)

    southBracket = makeBracket(south)
    levels = []
    southWinner, southLevels = getRegionalBracket(southBracket, levels, salaries)

    eastBracket = makeBracket(east)
    levels = []
    eastWinner, eastLevels = getRegionalBracket(eastBracket, levels, salaries)

    midwestBracket = makeBracket(midwest)
    levels = []
    midwestWinner, midwestLevels = getRegionalBracket(midwestBracket, levels, salaries)

    # now resolve the final four
    # south vs. east
    leftWinner = chooseWinner((southWinner, eastWinner), salaries)
    # midwest vs. west
    rightWinner = chooseWinner((midwestWinner, westWinner), salaries)

    # and our final winner!
    winner = chooseWinner((leftWinner, rightWinner), salaries)

    # put the final four info together
    # so we can print those last games
    finalTeams = [southWinner, eastWinner, midwestWinner, westWinner]
    finalLevels = [[(leftWinner, rightWinner)]]

    # how many of the games were decided by one methodo or another?
    print("Number of games decided by salaries: ", salaryChoices)
    print("Number of games decided lacking salary info: ", randomChoices)

    avgSalary = sum([v for k, v in salaries.items()]) / len(salaries)
    print("Average Salary: $%5.3fM" % (avgSalary/1e6))

    # print each regional bracket and the final four using ASCII art
    printLevels("West Bracket", west, westLevels, westWinner, salaries)
    printLevels("South Bracket", south, southLevels, southWinner, salaries)
    printLevels("East Bracket", east, eastLevels, eastWinner, salaries)
    printLevels("Midwest Bracket", midwest, levels, midwestWinner, salaries)
    printLevels("Final Four Bracket", finalTeams, finalLevels, winner, salaries)


def main():
    fn = sys.argv[1]
    predictMarchMadness(fn)

if __name__ == "__main__":
    main()