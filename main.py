from profit_loss import netprofitdifferences 
from cash_on_hand import cashdifferences
from overheads import overhead_func

with open('summary_report.txt','w') as file:
    file.write('Summary Report\n')
    file.write('=============================================\n')

overhead_func()
cashdifferences()
netprofitdifferences()