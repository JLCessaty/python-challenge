# import modules
import os
import csv

#pull data from CSV into budgetData with os.path.join

budgetData = os.path.join("resources", "budget_data.csv")

#open file

with open(budgetData, 'r') as file:

    budgetReader= csv.reader(file, delimiter =",")

    print(budgetReader)

    # read header

    budgetHead = next(budgetReader)
    print(f"Header: {budgetHead}")

    #set pieces
    
    firstList = []
    rowCount = 0
    totalProfit = 0
    changes1 = [0]
    months = []
    change = [0]
    changes = [0]
    total = 0
    
    #set for loop to loop through rows
    for row in budgetReader:
        
        #set rowCounter
        rowCount += 1

        #make changes1 to hold the value of the rows
        changes1.append(row[1])
        months.append(row[0])
        #set variables for index locations of current row and previous row
        prevRowVal = changes1[int(rowCount - 1)]
        currentRowVal = changes1[int(rowCount)]

        #calculate total profit
        totalProfit += int(row[1])
        
        #print the rows
        #print((row[0]), " ", (row[1]))
        
        #calculate month to month changes, and add value to changes
        if rowCount > 1:
            changes.append(int(currentRowVal) - int(prevRowVal))
    
    #set greatest and least value holders
    gvalueHolder = 0
    lvalueHolder = 0
    valueCounter = 0

    #check values of changes against set greatests and leasts
    for value in changes:
        total += value
        currentValue = int(changes[valueCounter])
        valueCounter +=1
        lastValue = int(changes[valueCounter - 1])
        
        if gvalueHolder < currentValue: 
            gvalueHolder = currentValue
            monthG = months[valueCounter - 1]
            
        if lvalueHolder > currentValue:
            lvalueHolder = currentValue
            monthL = months[valueCounter - 1]
            
                    
    average = total/ (rowCount - 1)

pyBankOutput = os.path.join("PyBank1.txt")

with open(pyBankOutput, 'w') as csvfile:

    #csvwriter
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months: " f"{len(changes)}"])
    csvwriter.writerow(["Total: " f"${totalProfit}"])
    csvwriter.writerow(["Average Change: " f"${average:.2f}"])
    csvwriter.writerow(["Greatest Increase in Profits: " f"{monthG}" f" (${gvalueHolder})"])
    csvwriter.writerow(["Greatest Decrease in Profits: " f"{monthL}" f" (${lvalueHolder})"])

