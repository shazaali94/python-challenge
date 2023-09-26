import csv
import os
# Initialize variables
#file_to_output = os.path.join("analysis", "budget_analysis.txt")
file_to_output = "budget_analysis.txt"
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}
# Read the CSV file
with open("PyBank/Resources/budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csvreader)
    
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate total number of months and net total
        total_months += 1
        net_total += profit_loss
        
        # Calculate change in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            
            # Check for greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print the results
analysis_text = (
    f"Financial Analysis\n"
    f"----------------------------\n"

f"Total Months: {total_months}\n"
f"Total: ${net_total}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)
# Print the analysis to the terminal
print(analysis_text)
# Export the results to a text file
with open(file_to_output , 'w') as txtfile:
    txtfile.write(analysis_text)

print(f"Results exported to {analysis_text}")