import os
import csv


in_folder="Resources"
in_file="budget_data.csv"


csvpath=os.path.join(in_folder,in_file)

print(csvpath)

# Initialize row count
nrows=0
net_total=0
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    print(csvreader)

    csv_header=next(csvreader)
    print(f"CSV file header: {csv_header}")

    for row in csvreader:
        print(row)