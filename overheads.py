from pathlib import Path
import csv

pl = Path.cwd()/"csv_reports/Overheads.csv"
with pl.open(mode="r", encoding="UTF-8", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header row of CSV File

    # create an empty dictionary for overhead
    overhead={}

    for row in reader:
        overhead[row[0]]=float(row[1]) #we convert the numbers from string to float so that we are able to compare them better
        
def overhead_func():
    with open('summary_report.txt','a') as file:
        file.write(f"\n[HIGHEST OVERHEAD] {max(overhead,key=overhead.get).upper()}: {overhead[max(overhead,key=overhead.get)]}%\n")
        #max(overhead,key=overhead.get) looks through every value in the dictionary and returns the key relating to the maximum value
        #we use this key again to obtain the maximum value using overhead[__] 