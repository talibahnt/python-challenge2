#Must Dos Example:

#Import Modules:
import os
import csv

#Enter input #Optional Code for problems below
star = input("Did you attend the MET Gala?"

#Create Path:
csvpath = os.path.join("Resources", "hollywood_stars.csv")

#If hollywood star attended the MET Gala #Opitonal
found = False

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the hollywood star
    for row in csvreader:
        if row[0] == star:
            print(row[0] + " attended by " + row[1] + " in " + row[2])

            # Set variable to confirm that we found out whether or not the hollywood star attended #Optional code for the problems below
            found = True

    # If the hollywood star is never found (did not attend), then follow up. #Optional
    if found is False:
        print("Sorry you did not attend this year. Hope to see you next year!")
        
#Open and Read file
with open(hollywood_star.csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Open and Write on output file

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    
print results






# python-challenge2
PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)



PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

Your analysis should align with the following results:
