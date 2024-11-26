# This is the file where I will keep all my code for the Module_3 assignment
import csv
import os

csvpath = os.path.join("Resources", "pybank.csv")

with open('./resources/pybank.csv', newline='') as csvfile:
    bankreader = csv.reader(csvfile, delimiter=',')
    months_processed = []
    num_months = 0 
    total = 0
    previous_profit = 0
    changes = []
    grt_p = [0, ""]
    grt_d = [0, ""]
    for row in bankreader:
        # telling loop to ignore header row
        if num_months == 0:
            num_months = num_months + 1 
            continue
        profit_num = int(row[1])
        # reomoves duplicte rows if necessary
        if row[0] not in months_processed:
            num_months = num_months + 1 
            months_processed.append(row[0])
        # changed row to integer to run code!
        total = total + profit_num
        # for average of averages!
        if previous_profit != 0:
            change = profit_num - previous_profit
            changes.append(change)
             
            if grt_p[0] < change:
                grt_p[0] = change
                grt_p[1] = row[0]
                
            if grt_d[0] > change:
                grt_d[0] = change 
                grt_d[1] = row[0]
                
        previous_profit = profit_num  
    # removing header count   
    num_months = num_months - 1
    
    average_change = sum(changes) / len(changes)

    #built to split and reverse the dfate column to return month then day
def split_and_reverse(item:str):
    return "-".join(list(reversed(item.split("-"))))

print("Finanical Analysis")
print("----------------------------")
print("Total Months: {}".format(num_months))
print("Total: ${}".format(total))
print("Average Change: ${}".format(round(average_change, 2)))
print("Greatest Increase in Profits: {} (${})".format(split_and_reverse(grt_p[1]), grt_p[0]))
print("Greatest Decrease in Profits: {} (${})".format(split_and_reverse(grt_d[1]), grt_d[0]))

    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

