import os
import csv

filepath_vote = os.path.join("GitHub","UT-TOR-DATA-PT-09-2019-U-C","Unit 3 - Python","Homework","Instructions","PyBank","Resources","budget_data.csv")
total = 0
months = []
var2= 0
var1 = 0
changes = []
with open(filepath_vote, 'r', newline = '') as file:
    read_file = csv.reader(file, delimiter=",")
    header = next(read_file)
    
    for row in read_file:
        months.append(row[0])
        total = total + int(row[1])
        var2 = var1
        var1 = row[1]
        change = int(var1) - int(var2)
        changes.append(int(change))
avg_changes = sum(changes) / len(changes)

maxchangemonth = changes.index(max(changes))
minchangemonth = changes.index(min(changes))

print("-------------------------------------------------")
print("Total Months: " + str(len(months)))
print ("Total: $" + str(total))
print("Average Change: " + str(avg_changes))
print(str(months[maxchangemonth]) + ": " + str(max(changes)))
print(str(months[minchangemonth]) + ": " + str(min(changes)))
