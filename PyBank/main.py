# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank", "resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank", "analysis", "budget_analysis.txt")  # Output file path


# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
monthly_profit_change = []
months = []
profit_losses = []
greatest_increase = 0
greatest_decrease = 0
monthly_increase = 0
monthly_decrease = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    my_rows = [1,2]
    my_rows.pop(0)

    # Process each row of data
    for row in reader:
       #budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})
        months.append(row[0])
        profit_losses.append(int(row[1]))

    # Track the total months
    total_months = len(months)

    #tracking net change
    total_net = sum(profit_losses)

# Iterate through the profits in order to get the monthly change in profits
    for i in range(len(profit_losses)-1):

# Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(profit_losses[i+1]-profit_losses[i])


# Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(monthly_profit_change)

# Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
        monthly_increase = monthly_profit_change.index(max(monthly_profit_change)) + 1
        monthly_decrease = monthly_profit_change.index(min(monthly_profit_change)) + 1


# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_losses)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {months[monthly_increase]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {months[monthly_decrease]} (${(str(greatest_decrease))})")

# Generate the output summary
file_to_output = os.path.join("PyBank", "analysis", "budget_analysis.txt")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:

    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Months: {len(months)}")
    txt_file.write("\n")
    txt_file.write(f"Total: ${sum(profit_losses)}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: {months[monthly_increase]} (${(str(greatest_increase))})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: {months[monthly_decrease]} (${(str(greatest_decrease))})")