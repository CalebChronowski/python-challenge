#Dependencies
import os
import csv

#CSV Path
csv_path = os.path.join("Resources", "election_data.csv")


#Create empty lists and variables  
candidate , vote = [], []
total = 0
n = 0

#Open the CSV
with open(csv_path, newline="") as csvfile:
    data = csv.reader(csvfile)

#Skip those pesky headers
    next(data, None)
    for row in data:
        if row[2] in candidate:
            vote[candidate.index(row[2])] += 1
            total += 1
        else:
            candidate.append(row[2])
            vote.append(1)
            total += 1

#OUTPUT
file = open('output.txt', "w")

for n in range(len(candidate)):
    print(candidate[n] + " " + str((round(100 * (vote[n] / total), 2))) + "% " + str(vote[n]))
    file.write(f"{candidate[n]} recieved {(round(100 * (vote[n] / total), 2))}% of the total vote with {vote[n]} total votes. ")

file.close()