#Dependencies
import os
import csv

#CSV Path
csv_path = os.path.join("Resources", "budget_data.csv")

#A place to store the dates when the max and min occur
max_date = 0
min_date = 0
max_profit = 0
min_profit = 0

#Create empty lists for storing column data and fill them in    
dates , values = [], []

#Open the CSV
with open(csv_path, newline="") as csvfile:
    data = csv.reader(csvfile)

#Skip those pesky headers    
    next(data, None)
    for row in data:
        dates.append(row[0])
        values.append(int(row[1]))
        if int(row[1]) > max_profit:
            max_profit = int(row[1])
            max_date = row[0]
        elif int(row[1]) < min_profit:
            min_profit = int(row[1])
            min_date = row[0]

#The math to find the values asked for in the assignment
month_count = len(dates)
net_profit = sum(values)
average_profit = net_profit/month_count
#max_profit = max(values)
#min_profit = min(values)


#find the max and min profit dates
#with open(csv_path, newline="") as csvfile:
    #data = csv.reader(csvfile)
    #while max_date == "x" and min_date == "x":
        #for row in data:
            #if row[1] == max_profit:
                #max_date = row[0]
           # elif row[1] == min_profit:
                #min_date = row[0]


#Print those values
print("--------------------------")
print("Financial Analysis")
print("--------------------------")
print("Months: ", str(month_count))
print("Net profit: ", str(net_profit))
print("Maximum monthly profit: ", max_date, " ", str(max_profit))
print("Minimum monthly profit: ", min_date, " ", str(min_profit))
print("--------------------------")

#Write results to file
file = open('output.txt', "w")
file.write("Financial Analysis ")
file.write(f"Months: {month_count} ")
file.write(f"Net profit: {net_profit} ")
file.write(f"Maximum monthly profit: {max_date} {max_profit} ")
file.write(f"Minimum monthly profit: {min_date} {min_profit}")
file.close()