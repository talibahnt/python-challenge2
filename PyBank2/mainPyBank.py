#Modules import the operating system and the excel file (csv/csv file)
import os
import csv

#files to load and output
#file_to_load = "Resources/budget_data.csv"
#file_to_output = "analysis/PyBank_2_Analysis.txt"

#Create a path for the csv file
PyBankcsvpath = os.path.join("Resources", "budget_data.csv")

#Create lists to store data and set counter values to 0.
#total number of months, net total profit/loss, average change profit/loss, greatest and decrease in profit variables
total_months = 0
total_profit = 0
previous_profit = 0
average_change = 0
date = []
profit = []
monthly_changes = []
profit_change_list = []
profit_changes = []
greatest_increase_profit = [" ", 0]
greatest_decrease_profit = [" ",99999999999999999999]

#Open csv file (budget_data.csv) using the defined path PyBankcsvpath
with open(PyBankcsvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Loop through each row in the dataset. Find the total number of months in the dataset. Monitor totals.
    for row in csvreader:

        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit"])
    
        #Monitor profit changes
        profit_changes = int(row["Profit"]) - previous_profit
        previous_profit = int(row["Profit"])
        monthly_changes = monthly_changes + [row["Date"]]

        #Calculate the greatest increase in profit. Use a conditional.
        if (profit_changes > greatest_increase_profit[1]):
            greatest_increase_profit[0] = row["Date"]
            greatest_increase_profit[1] = profit_changes

        #Calculate the greatest decrease in profit. Use a conditional.
        if (profit_changes < greatest_decrease_profit[1]):
            greatest_decrease_profit[0] = row["Date"]
            greatest_decrease_profit[1] = profit_changes

#Calculate the average change in profit. Total profit change divided number of profit change.
average_change = sum(profit_change_list) / len(profit_change_list)

#Provide the output (profit summary).Use f-strings.
output = (f"/nFinancial Analysis/n"
          f"--------------------------/n"
          f"Total Months: {total_months}/n"
          f"Total: ${total_profit}/n"
          f"Average Change: ${average_change}/n"
          f"Greatest Increase in Profit: {greatest_increase_profit[0]} (${greatest_increase_profit[1]})/n"
          f"Greatest Decrease in Profit: {greatest_decrease_profit[0]} (${greatest_decrease_profit[1]}/n)"
          )
    
#Print  output summary
print(output)

#Export and display result as a text (.txt) file in Microsoft Word.
PyBank_output_csvpath = os.path.join('analysis', 'PyBank_2_Financial_Analysis.txt')
with open(PyBank_output_csvpath, 'w', newline='') as textfile:
    textfile.write(output)