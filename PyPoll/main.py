
#
# Kate Spitzer
# UCSD Data Science and Visualization Bootcamp
# 9 Nov 2020 Cohort
#
# Python Homework  PYPOLL
# 9 Dec 2020
#

import csv


# set input filename
pypoll_csv = "c:/python-challenge/PyPoll/Resources/election_data.csv"


# initialize counters, accumulators and flags
total_votes = 0
most_votes = 0
election_cnts = {}

# open CSV file and assign pointer
with open(pypoll_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    next(csvreader)


    # loop through all rows in input file
    for row in csvreader:
        # read month and profit from current line
        candidate = row[2]

        if candidate not in election_cnts:
            election_cnts[candidate] = 1
        else:
            election_cnts[candidate] += 1

        
        total_votes += 1




# print analysis to console
print("\nElection Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
for candidate in election_cnts:
    percent_votes = format((election_cnts[candidate]/total_votes) * 100, ".3f")
    print(f"{candidate}: {percent_votes}% ({election_cnts[candidate]})")
    if election_cnts[candidate] > most_votes:
        most_votes = election_cnts[candidate]
        winner = candidate
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")



# set output filename
output_file = "C:/python-challenge/PyPoll/analysis/pypoll_analysis.txt"

# open the output file and write the
# analysis
with open(output_file, "w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("-----------------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("-----------------------------\n")
    for candidate in election_cnts:
        percent_votes = format((election_cnts[candidate]/total_votes) * 100, ".3f")
        datafile.write(f"{candidate}: {percent_votes}% ({election_cnts[candidate]})\n")        
        if election_cnts[candidate] > most_votes:
            most_votes = election_cnts[candidate]
            winner = candidate
    datafile.write("-----------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("-----------------------------\n")
