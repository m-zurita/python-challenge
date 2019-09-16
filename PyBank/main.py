# Imports
import os
import csv

# Variables
Total_Months = 0
ProfitLoss = 0
Changes = 0
InitialValue = 0
FinalValue = 0
TotalChange = 0
Check = False

#Open file in "read" mode
csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath, "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    # Calculations
    for row in csvreader:
        Total_Months += 1
        ProfitLoss += int(row[1])
        if Total_Months == 1:
            FinalValue = 0
        else:   
            FinalValue = int(row[1])
        Changes = (FinalValue-InitialValue)/85
        TotalChange = TotalChange + Changes
        InitialValue = int(row[1])
        if Check == False:
            GreatestIncrease = Changes*85
            DateIncrease = str(row[0])
            GreatestDecrease = Changes*85
            DateDecrease = str(row[0])
            Check = True
        else:
            if  Changes*85 > GreatestIncrease:
                GreatestIncrease = Changes*85
                DateIncrease = str(row[0])
                
            elif Changes*85 < GreatestDecrease:
                GreatestDecrease = Changes*85
                DateDecrease = str(row[0])


output_path = os.path.join("Results PyBank.txt")
with open(output_path, "w", encoding="utf-8", newline="\n") as txtfile:
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(["Financial Analysis"])
    txtwriter.writerow(["-----------------------------------"])
    txtwriter.writerow([f"Total Months: {Total_Months}"])
    txtwriter.writerow([f"Total: $ {ProfitLoss}"])
    txtwriter.writerow([f"Average Change: {round(TotalChange,2)}"])
    txtwriter.writerow([f"Greatest Increase in Profits: {DateIncrease} {round(GreatestIncrease,0)}"])
    txtwriter.writerow([f"Greatest Decrease in Profits: {DateDecrease} {round(GreatestDecrease,0)}"])

        
# Printing outputs in Python
print("Financial Analysis")
print("----------------------------------")
print("Total Months: ", Total_Months)
print("Total $", ProfitLoss)
print("Average Change: ", round(TotalChange,2))
print("Greatest Increase in Profits: ", DateIncrease, round(GreatestIncrease,0))
print("Greatest Decrease in Profits: ", DateDecrease, round(GreatestDecrease,0))