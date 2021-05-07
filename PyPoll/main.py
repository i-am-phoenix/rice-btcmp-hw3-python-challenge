import os
import csv

#  Input I/O file/folder names
in_folder="Resources"
in_file="election_data.csv"
out_file="election_data_analysis.txt"

#  Compile full input file path
csvpath=os.path.join(in_folder,in_file)
#print(csvpath)

# Initialize row count and unique candidate count
nrows=0
unq_candidates=[]

# read in and process the input data
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    
    # Skip the file header
    csv_header=next(csvreader)

    for row in csvreader:
        # Increment row count of rows containing data
        nrows+=1
        if row[2] not in unq_candidates:
            unq_candidates.append(row[2])
            #print(unq_candidates)

# Compile output file path
txtpath=os.path.join(in_folder,out_file)

# Open output file for writing and write first 4 lines
with open(txtpath,"w") as txtfile:
    txtfile.write("Election Results\n-------------------------\n")
    txtfile.write(f"Total Votes: {nrows}\n-------------------------\n")
 
#  Initialize vote counter per candidate 
init_cand_vote=0

# Loop through unique candidates to calculate and output stats
for c in range(len(unq_candidates)):
        ind_cand_vote=0
        
        # Open input file and read in data
        with open(csvpath) as csvfile:
            csvreader=csv.reader(csvfile,delimiter=",")

            # Skip the file header
            csv_header=next(csvreader)
            
            # With a given candidate name, loop through all rows in file and increment vote count if candidate name matches 
            for row in csvreader:
                if unq_candidates[c] in row:
                    ind_cand_vote+=1
            # Write out (append) current candidate's summary into the output file
            with open(txtpath,"a") as txtfile:        
                txtfile.write(f"{unq_candidates[c]}: {round(100*ind_cand_vote/nrows,4)}% ({ind_cand_vote})\n")
        # Check if current candidate's vote count total is greater than the current/previous vote total
        # If current candidate total votes is larger - declare curent candidate a winner 
        if ind_cand_vote>init_cand_vote:
            init_cand_vote=ind_cand_vote
            winner=unq_candidates[c]

 # Write out (append) name of the overall winner into the output file
with open(txtpath,"a") as txtfile:        
    txtfile.write("-------------------------\n")   
    txtfile.write(f"Winner: {winner}\n")   
    txtfile.write("-------------------------\n")   

# Printout entire summary by displaying the content of the output file within gitBash terminal standard output  
os.system(f"cat {txtpath}")