from pathlib import Path
import csv

pl = Path.cwd()/"csv_reports/Profits_and_Loss.csv"
with pl.open(mode="r", encoding="UTF-8", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header

    # create an empty list for profit and loss
    profitloss=[] 

    # append entries into the profitloss list
    for row in reader:
        #get the day, sales, trading profit, operating expense and net profit for each day and append to the profitloss list
        profitloss.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4])])
        
def netprofitdifferences():        
    netprofit=[] #creating an empty list
    for i in range(len(profitloss)): #appending all net profits values to the empty list
        netprofit.append(profitloss[i][4])

    netprofit_diff=[] #creating an empty list
    for i in range(len(netprofit)-1): #appending difference between 2 days to a list
        netprofit_diff.append(netprofit[i+1]-netprofit[i]) #we obtain one value and the value before it to find their difference

    #now to check if net profits is always increasing, decreasing, or fluctuating
    increase=0
    decrease=0
    for i in range(len(netprofit_diff)): #iterating through all net profit difference values
        if netprofit_diff[i]>0: increase+=1
        elif netprofit_diff[i]<0: decrease+=1
        
    with open('summary_report.txt','a') as file:
        if increase==len(netprofit_diff): #checking if net profit is constantly increasing in profits
            index=netprofit_diff.index(max(netprofit_diff)) #max(netprofit_diff) looks for the maximum value, netprofit_diff.index(__) gets the index of the maximum value in the list
            file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {profitloss[index][0]+1}, AMOUNT: SGD{max(netprofit_diff)}\n") #we used i+1 to help to iterate through the csv file to retrieve the value. 

        elif decrease==len(netprofit_diff): #is constantly decreasing in profits
            index=netprofit_diff.index(min(netprofit_diff)) #min(netprofit_diff) looks for the minimum value, netprofit_diff.index(__) gets the index of the minimum value in the list
            file.write("\n[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
            file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {profitloss[index][0]+1}, AMOUNT: SGD{-min(netprofit_diff)}\n") #since minimum is a negative value, we negate the negative sign
 
        else: #is fluctuating in profits
            #If net profit fluctuates, list down all the days and amount when deficit occurs, and find out the top 3 highest deficit amount and the days it happened.
            file.write("\nDays with Fluctuations in Net Profits:\n")
            deficit={} #using a dictionary to store all deficit days and values
            for i in range(len(netprofit_diff)): #iterating through all differences
                if netprofit_diff[i]<0: #is deficit as its a negative number
                    deficit[profitloss[i][0]+1]=netprofit_diff[i] #appending day and difference to the dictionary
                    file.write(f"[NET PROFIT DEFICIT] DAY: {profitloss[i][0]+1}, AMOUNT: SGD{-netprofit_diff[i]}\n")

            temp_list=sorted(netprofit_diff.copy()) #this sorts the difference list from smallest to largest values
            temp_list=temp_list[0:3] #obtaining the first 3 values of the sorted list the top 3 most negative values

            file.write("\nTop 3 Highest Deficit Amounts:\n")
            for i in range(3): #iterating through the 3 most negative values
                position=['','2ND ','3RD '] #to do the rankings for cash deficit values
                index=netprofit_diff.index(temp_list[i]) #temp_list[i] is the difference value, netprofit_diff.index(__) looks for its original position to correlate back to it's day
                file.write(f"[{position[i]}HIGHEST NET PROFIT DEFICIT] DAY: {profitloss[index][0]+1}, AMOUNT: SGD{-temp_list[i]}\n")