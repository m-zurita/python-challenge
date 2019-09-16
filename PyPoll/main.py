# Imports
import os
import csv

# Variables
TotalVotes = 0
CandidatePerc = []
CandidateDict = {}
NumDeCandidatos = 0
i = 0
Winner = []


# Open file in read mode
csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath, "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
# Calculations
    for row in csvreader:
        TotalVotes += 1
        if str(row[2]) in CandidateDict:
            CandidateDict[str(row[2])] += 1
        else:
            CandidateDict[str(row[2])] = 1
            NumDeCandidatos += 1


for x in CandidateDict:
    y = int(CandidateDict[x])/TotalVotes
    CandidatePerc.append(y)
WinningVotes = max(CandidateDict.values())

# Printing outputs in Python
print("Election Results")
print("-------------------------------------")
print("Total Votes: ", TotalVotes)
print("-------------------------------------")
for x in CandidateDict:
    print(x+":",str(round(CandidatePerc[i]*100,4))+"%", CandidateDict[x])
    i += 1
print("-------------------------------------")
print("Winner:", list(CandidateDict.keys())[list(CandidateDict.values()).index(WinningVotes)])
print("-------------------------------------")

i=0
output_path = os.path.join("Results PyPoll.txt")
with open(output_path, "w", encoding="utf-8", newline="\n") as txtfile:
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(["Election Results"])
    txtwriter.writerow(["-------------------------------------"])
    txtwriter.writerow([f"Total Votes: {TotalVotes}"])
    txtwriter.writerow(["-------------------------------------"])
    for x in CandidateDict:
        txtwriter.writerow([f"{x}: {str(round(CandidatePerc[i]*100,4))}% {CandidateDict[x]}"])
        i += 1
    txtwriter.writerow(["-------------------------------------"])
    txtwriter.writerow([f"Winner: {list(CandidateDict.keys())[list(CandidateDict.values()).index(WinningVotes)]}"])
    txtwriter.writerow(["-------------------------------------"])