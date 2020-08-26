import numpy as np;

oddSets = [[0.25, 0.18, 0.14, 0.125, 0.105, 0.07, 0.05, 0.04, 0.03, 0.01],
            [0.20, 0.17, 0.155, 0.135, 0.11, 0.08, 0.055, 0.045, 0.035, 0.015],
            [0.17, 0.15, 0.145, 0.135, 0.125, 0.095, 0.07, 0.05, 0.04, 0.02],
            [.38, .27, .24, .11],
            [.23, .245, .255, .27],
            [.075, .185, .24, .50],
            [.055, .11, .16, .675],
            [.04, 0.08, 0.10, 0.78],
            [0.015, 0.045, 0.075, 0.865],
            [0.005, 0.01, 0.03, 0.955]]
playerSlots = [[0,1,2,3,4,5,6,7,8,9],
            [0,1,2,3,4,5,6,7,8,9],
            [0,1,2,3,4,5,6,7,8,9],
            [0,1,2,3],
            [1,2,3,4],
            [2,3,4,5],
            [3,4,5,6],
            [4,5,6,7],
            [5,6,7,8],
            [6,7,8,9]]

teams = ['Brian', 'Liam', 'Bobby', 'Kevin', 'DJ', 'Carp', 'Rich', 'Jason', 'Patullo', 'Johnny'];

def draftLottery(teams):
    playerKey = {};
    playerIndexChosen = [];

    #First Choice Pick
    firstPick = randomPick(playerSlots[0], oddSets[0], teams);
    playerKey[firstPick] = 1;

    playerIndexChosen += [teams.index(firstPick)];

    #Second Choice Pick
    oddSets[1] = distributeOdds(oddSets[1], playerSlots[1], playerIndexChosen, playerKey);
    #playerSlots[1] = cleanUpSet(oddSets[1], playerSlots[1], playerIndexChosen, playerKey);
    secondPick = randomPick(playerSlots[1], oddSets[1], teams);
    playerKey[secondPick] = 2;

    playerIndexChosen += [teams.index(secondPick)];

    #Third Choice Pick
    oddSets[2] = distributeOdds(oddSets[2], playerSlots[2], playerIndexChosen, playerKey);
    #playerSlots[2] = cleanUpSet(oddSets[2], playerSlots[2], playerIndexChosen, playerKey);
    thirdPick = randomPick(playerSlots[2], oddSets[2], teams);
    playerKey[thirdPick] = 3;

    playerIndexChosen += [teams.index(thirdPick)];
    
    print(playerKey);

    lastPicks(oddSets, playerSlots, playerIndexChosen, playerKey, teams);
    print(playerKey);

    return 'Yo';

def lastPicks(oddSets, playerSlots, playerIndexChosen, playerKey, teams):
    pick = "";
    for i in range(9,2, -1):
        #oddSets[i] = distributeOdds(oddSets[i], playerSlots[i], playerIndexChosen, playerKey);
        distributeOdds(oddSets[i], playerSlots[i], playerIndexChosen, playerKey);
        #playerSlots[i] = cleanUpSet(oddSets[i], playerSlots[i], playerIndexChosen, playerKey);
        pick = randomPick(playerSlots[i], oddSets[i], teams);
        playerKey[pick] = i+1;

        playerIndexChosen += [teams.index(pick)];
    return 0

def randomPick(slotSet, oddSet, teams):
    # print(oddSet);
    # print(slotSet);
    winningIndex = np.random.choice(slotSet, 1, p = oddSet);
    winner = teams[winningIndex[0]];
    #print(winner);
    return winner;


def distributeOdds(oddSet, indexSet, chosenPlayers, playerKey):
    excessVal = 0;
    #Call to dictionary to check if players have been chosen already, add up the chosen probabilities to excess to distribute evenly
    indexSetCopy = indexSet[:];
    for i in indexSetCopy:
        if i in chosenPlayers:
            removeIndex = indexSet.index(i);
            excessVal += oddSet[removeIndex];
            oddSet.remove(oddSet[removeIndex]);
            indexSet.remove(indexSet[removeIndex]);
    #print(oddSet);
    excessVal = excessVal/len(oddSet);
    for i in range(len(oddSet)):
        oddSet[i] += float(excessVal);
    return oddSet;

# def cleanUpSet(oddSet, indexSet, chosenPlayers, playerKey):
#     indexSetCopy = indexSet[:];
#     for i in indexSetCopy:
#         if i in chosenPlayers:
#             removeIndex = indexSet.index(i);
#             indexSet.remove(indexSet[removeIndex]);
#     print(indexSet);
#     return indexSet;

draftLottery(teams);