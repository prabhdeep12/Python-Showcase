import os
import csv

csvpath = "budget_data.csv"


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    
    
   
    for row in csvreader:
        print(row)

total_months = 0
total = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 1000000000000]

month_of_change = []
net_change_list = []


with open(csvpath) as rawdata:
    reader = csv.reader(rawdata)
    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total = total + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_months = total_months + 1
        total = total + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

report = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(report)

   # Specify the file to write to
output_path = os.path.join("PyBankAnswers.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

   # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

   # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

   # Write the second row
    csvwriter.writerow(['----------------------------',])

    csvwriter.writerow(['Total Months : '+str(total_months)])
    csvwriter.writerow(['Total : ' +str(total)])
    csvwriter.writerow(['Average Change : '+str(net_monthly_avg)])
    csvwriter.writerow(['Greatest Increase in Profits : ' +str(greatest_increase)])
    csvwriter.writerow(['Greatest Decrease in Profits : ' +str(greatest_decrease)])
