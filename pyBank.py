import csv
import os


csvpath = os.path.join("Desktop","Python_Challenge","budget_data.csv")

with open(csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    
    #Set total number of month count to zero.
    total_number_months = 0
    
    #Set sum equal to zero.
    sum2 = 0
    
    #Create a list for profits
    profit = [] 
    
    #Create a list for dates
    date = []
     

    #count total number of months and append it to the date list
    for row in csvReader:
        total_number_months = total_number_months + 1 
        date.append(row[0])
        #Tell python to ignore profit/losses, add total values and append it to the profit list
        if row[1] != "Profit/Losses":
            sum2 = sum2 + int(row [1]) 
            profit.append(int(row[1]))

    change = []
    #calculate the rate of change and append it to the change list
    for i in range(len(profit)-1):
        change.append(profit[i+1]-profit[i])

    avgSum = 0
    #calculate the average sum by first setting the value to zero, the variable will go through the range length of change.
    for i in range(len(change)):
        avgSum = avgSum + change [i]
    
    #Average sum is the total average sum divided by the change list
    avgSum=avgSum/len(change)
    
    #Caluclate the greatest incease in profits
    max = 0
    maxMonth = 0
    for i in range(len(change)):
        if change[i] > max:
            max = change[i]
            maxMonth = date[i+2]

    #Calculate the greatest decrease in profits
    min = max
    minMonth = 0
    for i in range(len(change)):
        if change[i] < min:
            min = change[i]
            minMonth = date[i+2]


print("Financial Analysis")
print("------------------------")
print("Total Months:", total_number_months-1)
print("Total: $", sum2)
print("Average Change: $", round(avgSum,2))
print("Greatest Increase in Profits:", maxMonth, "($", max, ")")
print("Greatest Decrease in Profits:", minMonth, "($", min, ")")

