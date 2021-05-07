# rice-btcmp-hw3-python-challenge
Current repository contains two projects where Python default capabilities were being utilized.

## PyBank: Analysis of financial records of a company; 

- In this challenge, we were tasked with creating a Python script for analyzing the financial records of a given company. We were give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 
- The task was to create a Python script that analyzes the records to calculate each of the following:
  - The total number of months included in the dataset
  - The net total amount of "Profit/Losses" over the entire period
  - The average of the changes in "Profit/Losses" over the entire period
  - The greatest increase in profits (date and amount) over the entire period
  - The greatest decrease in losses (date and amount) over the entire period

### Input data: 

The input file contained the following data:

* *Date* column containing date reference provided as a *string* of "Mmm-YYY" format;
* Profit/Losses column which contained numerical values for profits (>0) and losses (<0)  

<img src="C:\Users\troub\gitHub\rice-btcmp-hw3-python-challenge\PyBank\Analysis\input_data.JPG" alt="input_data" style="zoom:50%;" />

### Analysis and output:

Code utilized *for* loops to cycle through all available entries in order to identify rows with highest recorded profits and lowest recorded losses, while aggregating the "Profit/Losses" volumes for *Net Total* amount and *Average of the Changes* of "Profits/Losses" calculation. Corresponding value within the *Date* column was then noted for output.

Output file [**budget_data_analysis.txt**](Resources/budget_data_analysis.txt) was created to output analysis summary and its content is reflected below:

```
Financial Analysis
----------------------------

Total Months: 86
Total: $38382578
Average  Change: $446309.05
Greatest Increase in Profits: Feb-2012 ($1170593)
Greatest Increase in Profits: Sep-2013 ($-1196225) 
```

As we can see a total of 86 months of data was available to us, with a net total volume of  ~$38.4 millions.

Average of changes in "Profit/Losses" over the entire period was ~$446 thousands, with greatest increase in profits recorded in February 2012 (~ $1.17 million) followed by the greatest loss of ~$1.2 million in September of 2013.

## PyPoll: Modernization of a vote counting process of a small rural town



