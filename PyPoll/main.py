import os
import csv

filepath_vote = os.path.join("UT-TOR-DATA-PT-09-2019-U-C","Unit 3 - Python","Homework","Instructions","PyPoll","Resources","election_data.csv")


candidates = []
votes = 0
candvotes = {}


with open(filepath_vote, 'r', newline = '') as file:
    read_file = csv.reader(file, delimiter=",")
    header = next(read_file)
    
    for row in read_file:
        cand = row[2]
        votes = votes + 1
        if cand not in candidates:
            candidates.append(cand)
            candvotes[cand] = 1 
        else:
            candvotes[cand] = candvotes[cand] + 1


print("Election Results")
print(40*"-")
# Total number of votes 
print("Total number of votes cast: " + str(votes))
print(40*"-")
# Candidate names
print("Candidate names: " + str(candidates))
print(40*"-")
# Percentage of vote for each candidate
print("Khan Vote %:" + str(round(candvotes['Khan']/votes,3)*100) + "%")
print("Correy Vote %:" + str(round(candvotes['Correy']/votes,3)*100) + "%")
print("Li Vote %:" + str(round(candvotes['Li'] /votes * 100,3)) + "%")
print("O'Tooley Vote %:" + str(round(candvotes["O'Tooley"]/votes,3)*100) + "%")
print(40*"-")
# Vote count
print("Khan vote count: " + str(candvotes['Khan']))
print("Correy vote count: " + str(candvotes['Correy']))
print("Li vote count: " + str(candvotes['Li']))
print("O'Tooley vote count: " + str(candvotes["O'Tooley"]))
print(40*"-")
# Winner of election based on Popular vote
if candvotes["Khan"]<candvotes["Correy"]:
    print("Winner: Correy")
elif candvotes["Khan"]<candvotes["Li"]:
    print("Winner: Li")
elif candvotes["Khan"]<candvotes["O'Tooley"]:
    print("Winner: O'Tooley")
else:
    print("Winner: Khan")
    
