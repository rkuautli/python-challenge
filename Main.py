import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
prev_profit_loss = 0
total_change = 0
average_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
change_list = []

# Read in the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    csv_header = next(csvreader)
    
    # Process each row in the CSV
    for row in csvreader:
        # Calculate total number of months
        total_months += 1
        
        # Calculate net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])
        
        # Calculate change from current month to previous month
        if total_months > 1:
            current_change = int(row[1]) - prev_profit_loss
            change_list.append(current_change)
        
        # Update previous profit/loss for next iteration
        prev_profit_loss = int(row[1])
        
        # Calculate greatest increase in profits (date and amount)
        if current_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = current_change
        
        # Calculate greatest decrease in profits (date and amount)
        if current_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = current_change

# Calculate average change
if len(change_list) > 0:
    total_change = sum(change_list)
    average_change = round(total_change / len(change_list), 2)

# Print results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export results to text file
output_path = os.path.join('output', 'financial_analysis.txt')
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
