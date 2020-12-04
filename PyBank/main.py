
import csv

pybank_csv = "c:\\python-challenge\\Pybank\\Resources\\budget_data.csv"

month_count = 0
net_profit = 0
total_change = 0
greatest_incr = 0
greatest_decr = 0

# Use encoding for Windows
with open(pybank_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    next(csvreader)

    for row in csvreader:
        month = row[0]
        change = int(row[1])

        if month_count > 0:
            total_change += change

        net_profit += change

        if change > greatest_incr:
            greatest_incr = change
            incr_month = month
        elif change < greatest_decr:
            greatest_decr = change
            decr_month = month

        month_count += 1


avg_change = total_change/month_count - 1

print("\nFinancial Analysis")
print("-----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {incr_month} (${greatest_incr})")
print(f"Greatest Decrease in Profits: {decr_month} (${greatest_decr})")



# Set variable for output file
output_file = "C:\\python-challenge\\PyBank\\analysis\\pybank_analysis.txt"

#  Open the output file
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("-----------------------------\n")
    datafile.write(f"Total Months: {month_count}\n")
    datafile.write(f"Total: ${net_profit}\n")
    datafile.write(f"Average Change: ${avg_change}\n")
    datafile.write(f"Greatest Increase in Profits: {incr_month} (${greatest_incr})\n")
    datafile.write(f"Greatest Decrease in Profits: {decr_month} (${greatest_decr})\n")
