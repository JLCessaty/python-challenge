#import modules
import os
import csv

#pull data from csv into electionData 
electionData = os.path.join("resources", "election_data.csv")

print(electionData)

with open(electionData, 'r') as file:
    electionReader = csv.reader(file, delimiter =",")
    print(electionReader)

    electionHead = next(electionReader)
    print(f"Header: {electionHead}")


    #set variables

    lastCand = ""
    currentCand = ""
    candidateList = []
    candidateList2 = []
    totalCand = 0
    voteTally1 = 0
    voteTally2 = 0
    voteTally3 = 0
    totalVotes = 0
    
    #count total votes and votes per candidate
    for row in electionReader:
        
        if currentCand == row[2]:
            totalVotes += 1
        elif currentCand != row[2]:
            candidateList.append(row[2])
            candidateList2.append(row[2])
            currentCand = row[2]
            totalVotes +=1
        if row[2] == "Charles Casper Stockham":
            voteTally1 += 1
        elif row[2] == "Diana DeGette":
            voteTally2 += 1
        elif row[2] == "Raymon Anthony Doane":
            voteTally3 += 1

    lstLoop = 0
    controller = 1
    otherLoop = 1
    firstPosCand = ""
    finalList = []
    
    #check looping candidate variable against candidates in candidateList to remove duplicates
    for cand in candidateList:
        candidate = cand
        
        for cand in candidateList:
            
            if lstLoop > controller and candidate == cand:
                candidateList.pop(lstLoop)
            lstLoop += 1
            
        lstLoop = 0 
        controller = 1

    # calculate percentage of votes
    candOnePerc = voteTally1 / totalVotes
    candTwoPerc = voteTally2 / totalVotes
    candThrPerc = voteTally3 / totalVotes

pyPollOutput = os.path.join("PyPoll1.txt")

with open(pyPollOutput, 'w') as csvfile:

    #csvwriter
    csvwriter = csv.writer(csvfile, delimiter=",")

    #file output contents
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow([f"Total Votes: " f"{totalVotes}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"{candidateList[0]} :"  f" {candOnePerc:.3%} "  f"({voteTally1})"])
    csvwriter.writerow([f"{candidateList[1]} :"  f" {candTwoPerc:.3%} "  f"({voteTally2})"])
    csvwriter.writerow([f"{candidateList[2]} :"  f" {candThrPerc:.3%} "  f"({voteTally3})"])
    csvwriter.writerow(["-------------------------"])    
    if voteTally1 > voteTally2 and voteTally1 > voteTally3:
        csvwriter.writerow(["Winner: "  f"{candidateList[0]}"])
    elif voteTally2 > voteTally1 and voteTally2 > voteTally3:
        csvwriter.writerow(["Winner: " f"{candidateList[1]}"])
    else:
        csvwriter.writerow(["Winner: "  f"{candidateList[2]}"])
    csvwriter.writerow(["-------------------------"])
