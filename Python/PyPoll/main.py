#import dependencies needed
import csv
import os

#reference my csv file
csvpath = os.path.join('Resources', 'election_data.csv')
#specify file to output
outputpath = os.path.join("output", "summary.csv")

candidates = {}

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first and then skip it
    csv_header = next(csvreader)
    
    for row in csvreader:
        #check if candidate exists and then count votes
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
    
    #get total votes
    totalvotes = sum(candidates.values())
    #get Key(candidate) with highest value
    winner = max(candidates, key=candidates.get)
    
    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(totalvotes))
    print('-------------------------')
    for k,v in candidates.items():
        print(str(k) + ': ' + str("{:.3%}".format(v/totalvotes)) +'% ('+ str(v) +')')
    print('-------------------------')
    print('Winner: '+str(winner))
    print('-------------------------')

# Open the output file
with open(outputpath, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')
    
    #write each row
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Total Votes: ' + str(totalvotes)])
    csvwriter.writerow(['-------------------------'])
    for k,v in candidates.items():
       csvwriter.writerow([(str(k) + ': ' + str("{:.3%}".format(v/totalvotes)) +'% ('+ str(v) +')')])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Winner: '+str(winner)])
    csvwriter.writerow(['-------------------------'])