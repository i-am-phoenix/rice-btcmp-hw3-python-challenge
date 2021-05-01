import os
import csv

in_folder="Resources"
in_file="election_data.csv"
out_file="election_data_analysis.txt"

csvpath=os.path.join(in_folder,in_file)
#print(csvpath)

# Initialize row count
nrows=0
unq_candidates=[]
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #print(csvreader)

    csv_header=next(csvreader)
    #print(f"CSV file header: {csv_header}")

    for row in csvreader:
        # Increment row count of rows containing data
        nrows=nrows+1
        if row[2] not in unq_candidates:
            unq_candidates.append(row[2])
            #print(unq_candidates)

#print(unq_candidates)
csvfile.close()

txtpath=os.path.join(in_folder,out_file)
# Open file for writing
with open(txtpath,"w") as txtfile:
    txtfile.write("Election Results\n-------------------------\n")
    txtfile.write(f"Total Votes: {nrows}\n-------------------------\n")
    # txtfile.write(f"Total: ${net_total}\n")
    # txtfile.write(f"Average  Change: ${round(net_total/nrows,2)}\n")
    # txtfile.write(f"Greatest Increase in Profits: {inc_mnth} (${gr_inc})\n")
    # txtfile.write(f"Greatest Increase in Profits: {dec_mnth} (${gr_dec})")
txtfile.close()
init_cand_vote=0
# print(len(unq_candidates))
for c in range(len(unq_candidates)):
        ind_cand_vote=0
        #print(unq_candidates[c])
        with open(csvpath) as csvfile:
            csvreader=csv.reader(csvfile,delimiter=",")
            #print(csvreader)

            csv_header=next(csvreader)
            #print(f"CSV file header: {csv_header}")
   
            for row in csvreader:
                
                if unq_candidates[c] in row:
                    ind_cand_vote=ind_cand_vote+1
                    #print(f"{unq_candidates[c]} - {ind_cand_vote} votes")
            with open(txtpath,"a") as txtfile:        
                txtfile.write(f"{unq_candidates[c]}: {round(100*ind_cand_vote/nrows,4)}% ({ind_cand_vote})\n")
        if ind_cand_vote>init_cand_vote:
            init_cand_vote=ind_cand_vote
            winner=unq_candidates[c]

with open(txtpath,"a") as txtfile:        
    txtfile.write("-------------------------\n")   
    txtfile.write(f"Winner: {winner}\n")   
    txtfile.write("-------------------------\n")    
os.system(f"cat {txtpath}")