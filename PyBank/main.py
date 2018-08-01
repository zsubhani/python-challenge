# This is main.py for PyBank by Zeshaun Subhani

import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip first row to not look at 'Date' and 'Revenue' 
    next(csvreader, None)
    
    # initialize total_num_of months
    total_num_of_months = 0
    # initialize total_net_amount_of_revenue
    total_net_amount_of_revenue = 0
	# initialize previous_month_profit_loss
    previous_month_profit_loss = 0
    # initialize greatest_increase_month
    greatest_increase_month = "Jan-18"
    # initialize greatest_decrease_month
    greatest_decrease_month = "Jan-18"
    # initialize greatest increase amount in profits
    greatest_increase_amount = 0
	# initialize greatest descrease amount in losses
    greatest_decrease_amount = 0
    # initialize total_profit_loss_change
    total_profit_loss_change = 0
    # set first_month_profit_loss_change to True. Then after first time through loop, it will get set to False because we will skip this value when calculating total profit loss change
    first_month_profit_loss_change = True
    
    # Loop through the data to calculate total number of months, total net amount of revenue, greatest increase amount, and greatest decrease amount
    for row in csvreader:
        
        # calculate total_num_of months. Since each row correponds to a new month, just add 1 to total_num_of_months for each row
        total_num_of_months += 1
        
        # calculate total_net_amount_of_revenue. keep adding value in 2nd column for each row
        total_net_amount_of_revenue = total_net_amount_of_revenue + int(row[1])
		
		# create a new column that will hold profit/loss change values from previous month
		# profit/loss change will be value of current month profit/loss - previous_month_profit_loss
        profit_loss_change = int(row[1]) - previous_month_profit_loss
        row.append(profit_loss_change)
        # calculate total profit loss change
        # skip first month in total profit loss change calculation
        if first_month_profit_loss_change == False:
            total_profit_loss_change = total_profit_loss_change + row[2]
        else:
            # first time through loop it will be true so we don't want it in calculation. set it to False for next time through loop
            first_month_profit_loss_change = False
		# before going back through loop, set previous_month_profit_loss to value of current month profit/loss
        previous_month_profit_loss = int(row[1])

        # calculate greatest increase amount. keep checking value in newly created 3rd column to see if it is higher than the value from previous row
        if int(row[2]) >= greatest_increase_amount:
            greatest_increase_amount = int(row[2])
            # capture month string corresponding to when greatest increase amount occurred
            greatest_increase_month = row[0]
        
        # calculate greatest decrease amount. keep checking value in newly created 3rd column to see if it is lower than the value from previous row
        if int(row[2]) < greatest_decrease_amount:
            greatest_decrease_amount = int(row[2])
            # capture month string corresponding to when greatest decrease amount occurred
            greatest_decrease_month = row[0]
            


# Calculate average change in revenue over entire period of months, which is total_profit_loss_change
# divided by total number of months- 1 since excluding the first month
average_change_in_revenue = float(total_profit_loss_change/(total_num_of_months - 1))
# round average_change_in_revenue float value to 2 decimal places
average_change = (round(average_change_in_revenue, 2))

# change format of greatest_increase_month from 'Sep-15' to 'Sep-2015' for use later when printing Financial Analysis
split_greatest_increase_month_list = greatest_increase_month.split("-")
new_greatest_increase_month = split_greatest_increase_month_list[0] + "-" + "20" + split_greatest_increase_month_list[1]
# change format of greatest_decrease_month from 'Aug-14' to 'Aug-2014' for use later when printing Financial Analysis
split_greatest_decrease_month_list = greatest_decrease_month.split("-")
new_greatest_decrease_month = split_greatest_decrease_month_list[0] + "-" + "20" + split_greatest_decrease_month_list[1]


# print out Financial Analysis info to screen
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_num_of_months))
print("Total Net Amount: $" + str(total_net_amount_of_revenue))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + new_greatest_increase_month + " ($" + str(greatest_increase_amount) + ")")
print("Greatest Decrease in Profits: " + new_greatest_decrease_month + " ($" + str(greatest_decrease_amount) + ")")

# export txt file with Financial Analysis Results
with open("Financial_Analysis_Results.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print("Total Months: " + str(total_num_of_months), file=text_file)
    print("Total Net Amount: $" + str(total_net_amount_of_revenue), file=text_file)
    print("Average Change: $" + str(average_change), file=text_file)
    print("Greatest Increase in Profits: " + new_greatest_increase_month + " ($" + str(greatest_increase_amount) + ")", file=text_file)
    print("Greatest Decrease in Profits: " + new_greatest_decrease_month + " ($" + str(greatest_decrease_amount) + ")", file=text_file)

# End of main.py script

	
	
	
	

