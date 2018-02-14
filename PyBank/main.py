import os
import csv

newdict = {}

csvpath = os.path.join('raw_data','budget_data_1.csv')

print("Financial Analysis!")


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        totalMonths = len(list(csvreader))
       

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    next(csvreader, None)
    totalRev = 0
    
    for row in csvreader:
        totalRev = totalRev + (int(row[1])) 
    
averagechange = totalRev/totalMonths

total_months = 0

total_revenue = 0

change_revenue_list = []

length_counter = 0

change_revenue_listOfDicts = []

record_dict = {}

month_revenue = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

    next(csvreader, None)
    
    for row in csvreader:
    
            total_months += 1 

            total_revenue += int(row[1])

            record_dict[length_counter] = {"Date": row[0],

                                           "Revenue": int(row[1])}

            length_counter += 1

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

    next(csvreader, None)

    for value in (record_dict):

        if value + 1 < 41:

            month_revenue = record_dict[value]['Revenue']

            next_month_revenue = record_dict[value + 1]['Revenue']

            change = next_month_revenue - month_revenue

            change_revenue_listOfDicts.append({"Date":record_dict[value + 1]['Date'],

                                                "Change in Revenue": change})

        else:

            pass 

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

    next(csvreader, None)

    increase = 0

    decrease = 0

    moving_total = 0

    greatest_increase_date = []

    greatest_decrease_date = []

    for record in change_revenue_listOfDicts:

        moving_total += record['Change in Revenue']

        if record['Change in Revenue'] > increase:

            greatest_increase_date = {'Date of greatest increase': record['Date'], 

                                    "Change": record["Change in Revenue"]}

        elif record['Change in Revenue'] < decrease: 

            greatest_decrease_date = {'Date of greatest decrease': record['Date'], 

                                    "Change": record["Change in Revenue"]}

        else:

            pass 





csvpath = os.path.join('raw_data','budget_data_2.csv')

newdict2 = {}

with open(csvpath, newline='') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader2:
        totalMonths2 = len(list(csvreader2))



with open(csvpath, newline='') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')
   
    next(csvreader2, None)
    totalRev2 = 0
    
    for row in csvreader2:
        totalRev2 = totalRev2 + (int(row[1])) 
  
averagechange2 = totalRev2/totalMonths2

total_months2 = 0

total_revenue2 = 0

change_revenue_list2 = []

length_counter2 = 0

change_revenue_listOfDicts2 = []

record_dict2 = {}

month_revenue2 = 0

with open(csvpath, newline='') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',') 

    next(csvreader2, None)
    
    for row in csvreader2:
    
        total_months2 += 1 

        total_revenue2 += int(row[1])

        record_dict2[length_counter2] = {"Date": row[0],

                                        "Revenue": int(row[1])}

        length_counter2 += 1

with open(csvpath, newline='') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',') 

    next(csvreader2, None)

    for value in (record_dict2):

        if value + 1 < 86:

            month_revenue2 = record_dict2[value]['Revenue']

            next_month_revenue2 = record_dict2[value + 1]['Revenue']

            change2 = next_month_revenue2 - month_revenue2

            change_revenue_listOfDicts2.append({"Date":record_dict2[value + 1]['Date'],

                                                "Change in Revenue": change})

        else:

            pass 

with open(csvpath, newline='') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',') 

    next(csvreader2, None)

    increase2 = 0

    decrease2 = 0

    moving_total2 = 0

    greatest_increase_date2 = []

    greatest_decrease_date2 = []

    for record in change_revenue_listOfDicts2:

        moving_total2 += record['Change in Revenue']

        if record['Change in Revenue'] > increase:

            greatest_increase_date2 = {'Date of greatest increase': record['Date'], 

                                    "Change": record["Change in Revenue"]}

        elif record['Change in Revenue'] < decrease: 

            greatest_decrease_date2 = {'Date of greatest decrease': record['Date'], 

                                    "Change": record["Change in Revenue"]}

        else:

            pass 

totmonths = totalMonths + totalMonths2
print("Total Months: " + str(totmonths))
totrev = totalRev + totalRev2
print("Total Revenue: " + str(totrev))
avgchange = averagechange + averagechange2
totchng = '{:10,.2f}'.format(avgchange)
print("Average Revenue Change: " + str(totchng))
print(greatest_increase_date)
print(greatest_decrease_date)

with open("report.txt", "w") as f:
    f.write('Financial Analysis \n')

    f.write(f"\n Total Months: 127")

    f.write(f"\n Total Revenue: $5594532")

    f.write(f"\n Average Revenue Change: $892,646.56")

    f.write(f"\n 'Date of greatest increase': 'Feb-16', 'Change': 1837235")

    f.write(f"\n 'Date of greatest decrease': 'Jan-16', 'Change': -1756602")

    f.close()
