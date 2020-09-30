#main.py for PyBank Challenge

#importing Python modules to work with CSV files
import os
import csv

#setting up path to collect data from the Resources folder
budgetData_path = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')

#creating work lists to store the data file, months/dates and profit/losses
budgetDataCSV = []
budgetDataCSVMonth = []
budgetDataCSVAmount = []



#Read in the CSV data file
with open(budgetData_path, 'r') as PyBankFile:

    # split the data on commas
    csvreader = csv.reader(PyBankFile, delimiter=',')
    # print(csvreader) delete this later
    csvheader = next(csvreader)
    #print(f"header:{csvheader}")  you may delete later

    # loop through the data and populate new lists

    for row in csvreader:
        #adding data from the rows to the list
        budgetDataCSV.append(row)
        #adding date to the budgetDataCSVMonth list, it is at index 0 being 1st item
        budgetDataCSVMonth.append(row[0])
        #print(f"{budgetDataCSVMonth}")
        #adding amount to the list, it is at index 1 being the 2nd item
        budgetDataCSVAmount.append(row[1])
        #print(f"{budgetDataCSVAmount}")
         


#calculating the total number of months included in the dataset, declaring and initializing variable to hold total months
TotalMonths = 0
TotalMonths = len(budgetDataCSVMonth)
#print(f"Total number of months: {TotalMonths}")
        


#calculating the net total amount of "Profit/Losses" over the entire period which denotes revenue
# loop through the list budgetDataCSV for the month and amount, add each amount to the TotalPLRevenue
#declaring and initializing variable to hold total P/L revenue
#converting amount to integer for mathematical operations
TotalPLRevenue = 0

for month, amount in budgetDataCSV:
    TotalPLRevenue += int(amount) 
    #print(f"Total Revenue:{TotalPLRevenue}")

# calculating the average of the changes in "Profit/Losses" over the entire period
# creating and initializing new list to hold the difference in amounts so the average can be calculated
budgetDataCSVAmountDiff = []
AvgChngPL = 0

#loop through the data and for each amount from the budgetDataCSVAmount list, 
# subtract the amount from row below to get the difference and append it to the list budgetDataCSVAmountDiff

for amount in range(1,len(budgetDataCSVAmount)):
    budgetDataCSVAmountDiff.append(int(budgetDataCSVAmount[amount]) - int(budgetDataCSVAmount[amount-1]))

AvgChngPL = round(sum(budgetDataCSVAmountDiff) / len(budgetDataCSVAmountDiff), 2)
#print(f"Average change:{str(AvgChngPL)}")


#calculating the greatest increase in profits as well as the greatest decrease in losses
# greatest increase will be the maximum amount from the budgetDataCSVAmountDiff list
# greatest decrease will be the minimum amount from the budgetDataCSVAmountDiff list
# declaring and initializing variables to hold the greatest increase and greatest decrese amounts as well as months
GreatestIncrease = 0
GreatestIncreaseMonthIndex = [0]
GreatestIncreaseMonth = [0]
GreatestDecrease = 0
GreatestDecreaseMonthIndex = [0]
GreatestDecreaseMonth = [0]

GreatestIncrease = max(budgetDataCSVAmountDiff)
#print(f"Greatest Increase:{GreatestIncrease}")
GreatestIncreaseMonthIndex = budgetDataCSVAmountDiff.index(GreatestIncrease)
#print(f"GreatestIncreaseMonthIndex:{GreatestIncreaseMonthIndex}")

# incrementing index by 1 as the first value in budgetDataCSVAmountDiff started with second row
GreatestIncreaseMonth = budgetDataCSVMonth[GreatestIncreaseMonthIndex + 1]
#print(f"GreatestIncreaseMonth:{GreatestIncreaseMonth}")

GreatestDecrease = min(budgetDataCSVAmountDiff)
#print(f"Greatest Decrease:{GreatestDecrease}")
GreatestDecreaseMonthIndex = budgetDataCSVAmountDiff.index(GreatestDecrease)
#print(f"GreatestDecreaseMonthIndex:{GreatestDecreaseMonthIndex}")

# incrementing index by 1 as the first value in budgetDataCSVAmountDiff started with second row
GreatestDecreaseMonth = budgetDataCSVMonth[GreatestDecreaseMonthIndex + 1]
#print(f"GreatestDecreaseMonth:{GreatestDecreaseMonth}")


#printing the analysis to the terminal
print("Financial Analysis")
print("----------------------------------------------------")        
print(f"Total Months: {TotalMonths}")
print(f"Total: ${TotalPLRevenue}")
print(f"Average Change: ${AvgChngPL}")
print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})")
print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})")

#exporting the analysis to a text file
output = open(".\Analysis\PyBank.txt", "w")
output.write("Financial Analysis\n")
output.write("----------------------------------------------------\n")
output.write(f"Total Months: {TotalMonths}\n")
output.write(f"Total: ${TotalPLRevenue}\n")
output.write(f"Average Change: ${AvgChngPL}\n")
output.write(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})\n")
output.write(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})\n")
output.close()    
