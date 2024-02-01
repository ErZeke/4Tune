from pathlib import Path
import csv

pl = Path.cwd()/"csv_reports/Cash_on_Hand.csv"
with pl.open(mode="r", encoding="UTF-8", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header row of CSV file

    # create an empty list for day and cash on hand
    cash=[] 

    # append entries into the profitloss list
    for row in reader:
        #get the day, sales, trading profit, operating expense and net profit for each day
        #and append to the profitloss list
        cash.append([int(row[0]),int(row[1])])
      #defining a function to calculate and analyse the differences in daily cash on hand  
def cashdifferences(): 
    cash_values=[] #creating an empty list
    for i in range(len(cash)): #appending all cash on hand values to the empty list
        cash_values.append(cash[i][1])

    cash_diff=[] #creating an empty list
    for i in range(len(cash_values)-1): #appending values of difference between 2 days to a list
        cash_diff.append(cash_values[i+1]-cash_values[i]) #we obtain one value and the value before it to find their difference

    #now to check if cash differences is always increasing, decreasing, or fluctuating
    increase=0
    decrease=0
    for i in range(len(cash_diff)): #iterating through all cash difference values
        if cash_diff[i]>0: increase+=1 #an increase in cash from the previous day
        elif cash_diff[i]<0: decrease+=1 #a decrease in cash from the previous day
    
    with open('summary_report.txt','a') as file: 
        if increase==len(cash_diff): #is constantly increasing in cash
            index=cash_diff.index(max(cash_diff)) #max(cash_diff) looks for the maximum value, cash_diff.index(__) gets the index of the maximum value in the list
            file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write(f"[HIGHEST CASH SURPLUS] DAY: {cash_values[index][0]+1}, AMOUNT: SGD{max(cash_diff)}\n")

        elif decrease==len(cash_diff): #is constantly decreasing in cash
            index=cash_diff.index(min(cash_diff)) #min(cash_diff) looks for the minimum value, cash_diff.index(__) gets the index of the minimum value in the list
            file.write("\n[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
            file.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_values[index][0]+1}, AMOUNT: SGD{-min(cash_diff)}\n") #since minimum is a negative value, we negate the negative sign
        #using [index][0]+1 ensures that the counter starts at day 1 and not day 0 which would be misleading and lead to inaccurate data
        #this would allow us to continue to use the same iterator to ensure code efficiency.
        else: #is fluctuating in cash
            #If cash fluctuates, list down all the days and amount when deficit occurs, and find out the top 3 highest deficit amount and the days it happened.
            file.write("\nDays with Fluctuations in Cash on Hand:\n")
            deficit={} #using a dictionary to store all deficit days and values
            for i in range(len(cash_diff)): #iterating through all differences
                if cash_diff[i]<0: #is deficit as its a negative number
                    deficit[cash[i][0]+1]=cash_diff[i] #appending day and difference to the dictionary
                    file.write(f"[CASH DEFICIT] DAY: {cash[i][0]+1}, AMOUNT: SGD{-cash_diff[i]}\n")

            temp_list=sorted(cash_diff.copy()) #this sorts the difference list from smallest to largest values
            temp_list=temp_list[0:3] #obtaining the first 3 values of the sorted list, aka the 3 most negative values

            file.write("\nTop 3 Highest Deficit Amounts:\n")
            for i in range(3): #iterating through the 3 most negative values
                position=['','2ND ','3RD '] #rankings for cash deficit values
                index=cash_diff.index(temp_list[i]) #temp_list[i] is the difference value, cash_diff.index(__) looks for its original position to correlate back to it's day
                file.write(f"[{position[i]}HIGHEST CASH DEFICIT] DAY: {cash[index][0]+1}, AMOUNT: SGD{-temp_list[i]}\n")