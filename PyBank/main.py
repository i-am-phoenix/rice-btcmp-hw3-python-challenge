import os
import csv

in_folder="Resources"
in_file="budget_data.csv"
out_file="budget_data_analysis.txt"

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
        # Increment row count of rows containing data
        nrows=nrows+1
        # Calculate running net total of profit/losses
        net_total=net_total + int(row[1])
        # Run a check to find value of the maximum profit and note corresponding month
        if int(row[1])>gr_inc:
            gr_inc=int(row[1])
            inc_mnth=str(row[0])
        # Run a check to find value of the maximum loss and note corresponding month
        if int(row[1])<gr_dec:
            gr_dec=int(row[1])
            dec_mnth=str(row[0])
        

txtpath=os.path.join(in_folder,out_file)
# Open file for writing
with open(txtpath,"w") as txtfile:
    txtfile.write("Financial Analysis\n----------------------------\n")
    txtfile.write(f"Total Months: {nrows}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average  Change: ${round(net_total/nrows,2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {inc_mnth} (${gr_inc})\n")
    txtfile.write(f"Greatest Increase in Profits: {dec_mnth} (${gr_dec})")
txtfile.close()

# Two options for outputting analysis summary within the terminal:
# - through publication of the TXT file content
os.system(f"cat {txtpath}") 
# - or through explicit reporting into the terminal one-by-one
print("\nFinancial Analysis\n----------------------------")
print(f"Total Months: {nrows}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${round(net_total/nrows,2)}")
print(f"Greatest Increase in Profits: {inc_mnth} (${gr_inc})")
print(f"Greatest Increase in Profits: {dec_mnth} (${gr_dec})")

