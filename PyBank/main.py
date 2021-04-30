import os
import csv

in_folder="Resources"
in_file="budget_data.csv"

csvpath=os.path.join(in_folder,in_file)
#print(csvpath)

# Initialize row count
nrows=0
net_total=0
gr_inc=0
gr_dec=0
inc_mnth=""
dec_mnth=""
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #print(csvreader)

    csv_header=next(csvreader)
    #print(f"CSV file header: {csv_header}")

    for row in csvreader:
        #print(row)
        #print(row[1])
        nrows=nrows+1
        net_total=net_total + int(row[1])
        if int(row[1])>gr_inc:
            gr_inc=int(row[1])
            inc_mnth=str(row[0])
        if int(row[1])<gr_dec:
            gr_dec=int(row[1])
            dec_mnth=str(row[0])
        

print("Financial Analysis\n----------------------------")
print(f"Total Months: {nrows}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${round(net_total/nrows,2)}")
print(f"Greatest Increase in Profits: {inc_mnth} (${gr_inc})")
print(f"Greatest Increase in Profits: {dec_mnth} (${gr_dec})")