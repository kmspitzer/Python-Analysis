
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
        # read candidate name
        candidate = row[2]

        # if candidate is not in dictionary, add with value of 1 vote
        if candidate not in election_cnts:
            election_cnts[candidate] = 1
        else:
            # candidate already in dictionary, increment number of votes
            election_cnts[candidate] += 1

        # increment total number of votes cast
        # for all candidates
        total_votes += 1



# set output filename
output_file = "C:/python-challenge/PyPoll/analysis/pypoll_results.txt"

# open the output file and write the
# election results to file and console
with open(output_file, "w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("-----------------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("-----------------------------\n")

    print("\nElection Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")


    # loop through all candidates in dictionary
    for candidate in election_cnts:
        # calculates percent votes cast for the current candidate
        percent_votes = format((election_cnts[candidate]/total_votes) * 100, ".3f")

        # write formatted line to output file
        datafile.write(f"{candidate}: {percent_votes}% ({election_cnts[candidate]})\n")
        # print formatted line to console
        print(f"{candidate}: {percent_votes}% ({election_cnts[candidate]})")

        # grab candidate with the most votes
        if election_cnts[candidate] > most_votes:
            most_votes = election_cnts[candidate]
            winner = candidate

    # write the winner's name to the output file
    datafile.write("-----------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("-----------------------------\n")

    # print winner's name to console
    print("-----------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------\n")

