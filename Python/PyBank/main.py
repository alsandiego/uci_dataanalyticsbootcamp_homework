#import dependencies needed
import csv
import os

#reference my csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
#specify file to output
outputpath = os.path.join("output", "summary.csv")

dates = []
amount = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first and then skip it
    csv_header = next(csvreader)
    
    #creates a list and append each row in respective column
    for row in csvreader:
        dates.append(row[0])
        amount.append(int(row[1]))
    
    #get count of months and sum of profit/loss
    totalmonths = len(dates)
    totalamount = sum(amount)

#create another list to calculate values
profitlost_values = []
profit_date = []

for i in range(len(amount)):
    #skip the first row for its not needed to calculate its change in profit/loss
    if i >= 1 :
        #deduct current row from previous row
        profitlost_values.append((amount[i] - amount[i-1]))
        #append corresponding date row
        profit_date.append(dates[i])


avgvalue = sum(profitlost_values)/len(profitlost_values)
maxvalue = max(profitlost_values)
minvalue = min(profitlost_values)
maxdate = profit_date[profitlost_values.index(max(profitlost_values))] #find corresponding row based on maxvalue
mindate = profit_date[profitlost_values.index(min(profitlost_values))] #find corresponding row based on minvalue

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {totalmonths}')
print(f'Total: ${totalamount}')
print('Average  Change: $'+ str(round((avgvalue),2)))
print(f'Greatest Increase in Profits: {maxdate} (${maxvalue})')
print(f'Greatest Decrease in Profits: {mindate} (${minvalue})')

# Open the output file
with open(outputpath, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')
    
    #write each row
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f'Total Months: {totalmonths}'])
    csvwriter.writerow([f'Total: ${totalamount}'])
    csvwriter.writerow(['Average  Change: $'+ str(round((avgvalue),2))])
    csvwriter.writerow([f'Greatest Increase in Profits: {maxdate} (${maxvalue})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {mindate} (${minvalue})'])