# python-challenge

UCSD Data Science and Visualization Bootcamp - Python HW  9 Dec 2020


Collaborated with Rick Spitzer


This repository contains files pertaining to the Python Homework due 9 Dec 2020.



PyBank: This script reads in a .csv file containing monthly profit/loss data by month. Analysis is performed on data read and is printed
the console, as well as being written to an output file, analysis/pybank_analysis.txt.


Analysis consists of:


		Total number of months included in the dataset
		
		Net total amount of "Profit/Losses" over the entire period
		
		Change in "Profit/Losses" over the entire period, and the average of those changes is calculated
		
		Greatest increase in profits (date and amount) over the entire period
		
		Greatest decrease in losses (date and amount) over the entire period
		
		
   
     Output is in the following format:

         Financial Analysis
         ----------------------------
        Total Months: 86
        'Total: $38382578
         Average  Change: $-2315.12
         Greatest Increase in Profits: Feb-2012 ($1926159)
         Greatest Decrease in Profits: Sep-2013 ($-2196167)


 PyPoll: This script reads in a .csv file containing voting data for an election.  Each row of data represents one vote.  Analysis is performed
 on the data read and is printed to the console, as well as being written to an output file, analysis/py_results.txt.
 
 Analysis consists of:
 
	   Total number of votes cast
	
	   Complete list of candidates who received votes
	
	   Percentage of votes each candidate won
	
	   Total number of votes each candidate won
	
	   Winner of the election based on popular vote
	

     Output is in the following format:

         Election Results
         -------------------------
         Total Votes: 3521001
         -------------------------
         Khan: 63.000% (2218231)
         Correy: 20.000% (704200)
         Li: 14.000% (492940)
         O'Tooley: 3.000% (105630)
         -------------------------
         Winner: Khan
         -------------------------



 PyBoss:  This script reads in a .csv file containing employee data, reformats several of the columns, zips the new data back together and
 writes the newly formatted data to a new output .csv file, analysis/new_employee_data.csv.
 
 Input data consists of:
 
	       Emp ID
		 
	       Name
		 
	       DOB (in YYYY-MM-DD fomrat)
		 
	       SSN (in nnn-nnn-nnnn)
		 
	       State (spelled out in Title format)
		 

 Name, DOB, SSN and State need to be reformatted and written to the output file as follows:

	       Emp ID
		 
	       First Name
		 
	       Last Name
		 
	       DOB (in MM/DD/YYYY format)
		 
	       SSN (in ***-***-nnnn format)
		 
	       State (in 2 character abbreviation format

   NOTE: state abbreviation dictionary include from GitHub afhaque/us_state_abbrev.py



 PyParagraph:  This script reads in a text file, analyzes the data, and prints the results to the console, as well as writing to an
 output file, analysis/pyparagraph_analysis.txt.
 
 Analysis consists of:
 
	   Approximate word count
	
	   Approximate sentence count
	
	   Approximate letter count (per word)
	
	   Average sentence length (in words)
	

     Output is in the following format:

         Paragraph Analysis
         -----------------
         Approximate Word Count: 122
         Approximate Sentence Count: 5
         Average Letter Count: 4.6
         Average Sentence Length: 24.0











