import random
from fighters import *
from classes import *

def fight(matchup):
    redSigStrikes = matchup.red.skillLevel + random.randint(-20, 20)
    blueSigStrikes = matchup.blue.skillLevel + random.randint(-20, 20)
    splitDecision = random.randint(0,1)

    stylisticFinishProb = 65

    redFinishChance = 0.5 * matchup.red.skillLevel
    blueFinishChance = 0.5 * matchup.blue.skillLevel


    def finishtype(fighter):
        if fighter.style == 0:
            if random.randint(0, 100) <= stylisticFinishProb:
                return "KO"
            else:
                return "Submission"
        else:
            if random.randint(0, 100) <= stylisticFinishProb:
                return "Submission"
            else:
                return "KO"
    
    if random.randint(0, 100) <= redFinishChance:
        print(f"{matchup.red.name} finished {matchup.blue.name} by {finishtype(matchup.red)}")
        return matchup.red

    if random.randint(0, 100) <= blueFinishChance:
        print(f"{matchup.blue.name} finished {matchup.red.name} by {finishtype(matchup.blue)}")
        return matchup.blue

    if redSigStrikes > blueSigStrikes:
        print(f"{matchup.red.name} beat {matchup.blue.name} by decision")
        return matchup.red
    elif blueSigStrikes > redSigStrikes:
        print(f"{matchup.blue.name} beat {matchup.red.name} by decision")
        return matchup.blue
    else:
        if splitDecision == 0:
            print(f"{matchup.red.name} beat {matchup.blue.name} by split decision")
            return matchup.red
        else:
            print(f"{matchup.blue.name} beat {matchup.red.name} by split decision")
            return matchup.blue
    
def simulateRound(roundList, roundName):
    print(roundName)
    for i in roundList:
        i.winner = fight(i)

fight11 = Fight(seededfighters[0], seededfighters[15], "undetermined")
fight12 = Fight(seededfighters[1], seededfighters[14], "undetermined")
fight13 = Fight(seededfighters[2], seededfighters[13], "undetermined")
fight14 = Fight(seededfighters[3], seededfighters[12], "undetermined")
fight15 = Fight(seededfighters[4], seededfighters[11], "undetermined")
fight16 = Fight(seededfighters[5], seededfighters[10], "undetermined")
fight17 = Fight(seededfighters[6], seededfighters[9], "undetermined")
fight18 = Fight(seededfighters[7], seededfighters[8], "undetermined")

round1 = [fight11, fight12, fight13, fight14, fight15, fight16, fight17, fight18]

simulateRound(round1, "Round 1")

fight21 = Fight(fight11.winner, fight12.winner, "undetermined")
fight22 = Fight(fight13.winner, fight14.winner, "undetermined")
fight23 = Fight(fight15.winner, fight16.winner, "undetermined")
fight24 = Fight(fight17.winner, fight18.winner, "undetermined")

round2 = [fight21, fight22, fight23, fight24]

simulateRound(round2, "Quarter Finals")

fight31 = Fight(fight21.winner, fight22.winner, "undetermined")
fight32 = Fight(fight23.winner, fight24.winner, "undetermined")

round3 = [fight31, fight32]

simulateRound(round3, "Semi Finals")

championship = Fight(fight31.winner, fight24.winner, "undetermined")
Championship = [championship]

simulateRound(Championship, "Championship")

print(f"{championship.winner.name} is the Champion")