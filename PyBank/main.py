
#
# Kate Spitzer
# UCSD Data Science and Visualization Bootcamp
# 9 Nov 2020 Cohort
#
# Python Homework  PYBANK
# 9 Dec 2020
#
# Collaborated with Rick Spitzer
#

import csv


# set input filename
pybank_csv = "c:\\python-challenge\\PyBank\\Resources\\budget_data.csv"


# initialize counters, accumulators and flags
month_count = 0
net_profit = 0
total_change = 0
greatest_incr = 0
greatest_decr = 0
first_read = True



# open CSV file and assign pointer
with open(pybank_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    next(csvreader)


    # loop through all rows in input file
    for row in csvreader:
        # read month and profit from current line
        current_month = row[0]
        current_profit = int(row[1])

        # don't do calculations on the first
        # time through
        if first_read:
            first_read = False
        else:
            # calculation change from last month
            # to current month and accumulate total change
            # in profit
            change = current_profit - prev_profit
            total_change += change

            # capture greatest monthly increase
            # and greatest monthly decrease and
            # the months in which they occur
            if change > greatest_incr:
                greatest_incr = change
                incr_month = current_month
            elif change < greatest_decr:
                greatest_decr = change
                decr_month = current_month

        # accumulate net profit, save the current profit for
        # calculating change to the next month, and
        # increment the month counter
        net_profit += current_profit
        prev_profit = current_profit
        month_count += 1

# once we've finished reading all our data,
# calculate the average change across months
avg_change = total_change/(month_count - 1)


# print analysis to console
print("\nFinancial Analysis")
print("-----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {incr_month} (${greatest_incr})")
print(f"Greatest Decrease in Profits: {decr_month} (${greatest_decr})\n")



# set output filename
output_file = "C:\\python-challenge\\PyBank\\analysis\\pybank_analysis.txt"

# open the output file and write the
# analysis
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("-----------------------------\n")
    datafile.write(f"Total Months: {month_count}\n")
    datafile.write(f"Total: ${net_profit}\n")
    datafile.write(f"Average Change: ${round(avg_change,2)}\n")
    datafile.write(f"Greatest Increase in Profits: {incr_month} (${greatest_incr})\n")
    datafile.write(f"Greatest Decrease in Profits: {decr_month} (${greatest_decr})\n")
