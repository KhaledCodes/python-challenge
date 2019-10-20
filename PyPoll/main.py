import os
import csv

filepath_vote = os.path.join("GitHub","UT-TOR-DATA-PT-09-2019-U-C","Unit 3 - Python","Homework","Instructions","PyPoll","Resources","election_data.csv")

votes = []
candidates = []

with open(filepath_vote, 'r', newline = '') as file:
    read_file = csv.reader(file, delimiter=",")
    header = next(read_file)
    
    for row in read_file:
        votes.append(row)

print(len(votes))

