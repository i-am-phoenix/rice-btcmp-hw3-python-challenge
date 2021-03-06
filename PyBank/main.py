import os
import csv

# Set up I/O file naming structure
in_folder="Resources"
in_file="budget_data.csv"
out_file="budget_data_analysis.txt"

# Create a file path variable
csvpath=os.path.join(in_folder,in_file)
#print(csvpath)

# Initialize row count, net total, greatest increase and decrease and corresponding month identifiers
nrows=0
net_total=0
gr_inc=0
gr_dec=0
inc_mnth=""
dec_mnth=""

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    # skip the header prior to reading in the data
    csv_header=next(csvreader)

    for row in csvreader:
        # Increment row count of rows containing data
        nrows+=1
        # Calculate running net total of profit/losses
        net_total+= int(row[1])
        # Run a check to find value of the maximum profit and note corresponding month
        if int(row[1])>gr_inc:
            gr_inc=int(row[1])
            inc_mnth=str(row[0])
        # Run a check to find value of the maximum loss and note corresponding month
        if int(row[1])<gr_dec:
            gr_dec=int(row[1])
            dec_mnth=str(row[0])
        
# Generate output file name
txtpath=os.path.join(in_folder,out_file)

# Open output file for writing
with open(txtpath,"w") as txtfile:
    txtfile.write("Financial Analysis\n----------------------------\n")
    txtfile.write(f"Total Months: {nrows}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average  Change: ${round(net_total/nrows,2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {inc_mnth} (${gr_inc})\n")
    txtfile.write(f"Greatest Increase in Profits: {dec_mnth} (${gr_dec})")
txtfile.close()

# Two options for outputting analysis summary within the terminal:
# 1) through publication of the TXT file content into gitBash terminal
os.system(f"cat {txtpath}") 
# 2) or through explicit reporting into the terminal one-by-one
print("\nFinancial Analysis\n----------------------------")
print(f"Total Months: {nrows}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${round(net_total/nrows,2)}")
print(f"Greatest Increase in Profits: {inc_mnth} (${gr_inc})")
print(f"Greatest Increase in Profits: {dec_mnth} (${gr_dec})")