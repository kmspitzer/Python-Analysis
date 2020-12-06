
#
# Kate Spitzer
# UCSD Data Science and Visualization Bootcamp
# 9 Nov 2020 Cohort
#
# Python Homework  PYBOSS
# 9 Dec 2020
#
# NOTE: us_state_abbrev dictionary copied from GitHub open source repository afhaque/us_state_abbrev.py
#

import csv


# state abbreviation dictionary copied from GitHub
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}



# set input filename
pyboss_csv = "c:/python-challenge/PyBoss/Resources/employee_data.csv"



# create empty list to store reformatted data
employee_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []


# open inputfile for reading
with open(pyboss_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    next(csvreader)


    # loop through each row of data
    for row in csvreader:

        # add employee id to employee id list
        employee_id.append(row[0])

        # split name into first and last and add
        # to appropriate lists
        splitname = row[1].split()
        first_name.append(splitname[0])
        last_name.append(splitname[1])

        # split date of birth to remove hyphens and
        # reformat as MM/DD/YYYY
        splitdob = row[2].split("-")
        dob.append(splitdob[1] + "/" + splitdob[2] + "/" + splitdob[0])

        # split social security number so that we can use
        # save only the last 4 digits in out new table
        splitssn = row[3].split("-")
        ssn.append("***-***-" + splitssn[2])

        # grab state abbreviation out of dictionary and add
        # to our list
        state.append(us_state_abbrev[row[4]])

    
# zip lists together
newformat_csv = zip(employee_id, first_name, last_name, dob, ssn, state)

# set variable for output file
output_file = "c:/python-challenge/PyBoss/analysis/new_employee_data.csv"

#  open output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])

    # Write in reformatted zipped rows
    writer.writerows(newformat_csv)
