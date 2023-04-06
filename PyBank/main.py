# Python Code for PyBank

#Import the csv and os Modules
import csv
import os

#Set a path that leads to the budget_data.csv
budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#Set variables to gather pertinent information
months_list = []
profits_losses_list = []
total_months = 0
total_money = 0
avg_change_list = []
avg_change = 0
greatest_inc = 0
greatest_dec = 0
prev_year_change = 0
greatest_inc_month = []
greatest_dec_month = []

#Open the path that leads to the budget_data.csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Store the header of budget_data.csv
    csv_header = next(csv_reader)

    #Start a loop to look for pertinent information within budget_data.csv
    for row in csv_reader:

        months_list.append(row[0])
        profits_losses_list.append(row[1])

        #Count the number of months or rows
        total_months = total_months + 1

        #Store the value in the Profit/Losses column
        year_change = int(row[1])

        #Sum all the values in the Profit/Losses column
        total_money = total_money + year_change

        #Calculate the change between each year and store them as a list
        if total_months != 1:
            profit_lose = year_change - prev_year_change
            avg_change_list.append(profit_lose)

        #Reset the value for the previous year for the next loop
        prev_year_change = year_change

    #Calcule the average change over the timespan 
    avg_change = round(sum(avg_change_list)/(total_months-1),2)

    #Find the value of greatest increase in the average change list and storing it
    greatest_inc = max(avg_change_list)

    #Find the row number of the greatest increase and store it
    greatest_inc_row = avg_change_list.index(greatest_inc)

    #Find the date corresponding to the row number of the greatest increase and store it
    greatest_inc_month = months_list[greatest_inc_row + 1]

    #Find the value of greatest decrease in the average change list and storing it
    greatest_dec = min(avg_change_list)

    #Find the row number of the greatest decrease and store it
    greatest_dec_row = avg_change_list.index(greatest_dec)

    #Find the date corresponding to the row number of the greatest decrease and store it
    greatest_dec_month = months_list[greatest_dec_row + 1]

#Print the analysis to the terminal
print(f"Financial Analysis")
print(f"----------------------")
print(f"Total Months: {total_months}" )
print(f"Total: ${total_money:,}")
print(f"Average Change: ${avg_change:,}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc:,})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec:,})")


#Export a text file with the analysis
budget_data_output = os.path.join("PyBank", "Analysis", "budget_data.txt")
with open(budget_data_output, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------\n")
    txtfile.write(f"Total Months: {total_months}\n" )
    txtfile.write(f"Total: ${total_money:,}\n")
    txtfile.write(f"Average Change: ${avg_change:,}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc:,})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec:,})\n")
   