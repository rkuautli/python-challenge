import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
months = []

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)  # Skip header row

    # Iterate through the rows in the CSV
    for row in csvreader:
        # Calculate total number of months
        total_months += 1
        months.append(row[0])  # Collect the months
        
        # Calculate net total amount of Profit/Losses
        net_total += int(row[1])
        
        # Calculate change in profit from previous month to current month
        if total_months > 1:
            profit_change = int(row[1]) - previous_profit
            profit_changes.append(profit_change)
        
        previous_profit = int(row[1])

# Calculate average change in profit/losses
average_change = round(sum(profit_changes) / len(profit_changes), 2)

# Find greatest increase and decrease in profits
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Find corresponding months for greatest increase and decrease
increase_month = months[profit_changes.index(greatest_increase)]
decrease_month = months[profit_changes.index(greatest_decrease)]

# Print results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Write results to text file
output_file = os.path.join("analysis", "financial_analysis.txt")
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")
