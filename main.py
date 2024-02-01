#import  the neccessary modules from the different files
from profit_loss import netprofitdifferences 
from cash_on_hand import cashdifferences
from overheads import overhead_func

#open a file named 'summary_report.txt' in write mode
with open('summary_report.txt','w') as file:
    file.write('Summary Report\n')
    file.write('=============================================\n')

#call the function to report the respective modules
overhead_func()
cashdifferences()
netprofitdifferences()