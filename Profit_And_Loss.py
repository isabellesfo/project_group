# This line imports the operating system into the file.
import os

# This line imports "Path" from the "pathlib" module.
from pathlib import Path

# This line imports "csv" module and allows us to use the data from the csv files into this file. 
import csv

# This line of code calls "os.getcwd()" and assigns the returned path to the variable "original_working_dir".
original_working_dir= os.getcwd()

# This lines sets the current working directory to the folder containing the CSV file. 
csv_folder = os.path.join(os.getcwd(), "csv_reports")
os.chdir(csv_folder)

# This line opens and reads the CSV file.
csv_file = "Profit_And_Loss.csv"

# This opens and reads the csv file.
with open(csv_file, mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

# This skips the header row as it contains column names that are not needed. 
    next(reader)

# This assigns an empty list to the variable profit_and_loss.
    profit_and_loss = []

# This is a loop that will execute the code for each row of data in reader. 
    for row in reader:

# This appends the list for the code and creates a new list with a converted integer value.
        profit_and_loss.append([int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4])])

# This line defines the function "calculate_profit_loss_scenario1" which takes the argument "data". 
# This function determines if there is a profit surplus scenario within "data".
# Calculate Profit and Loss for Scenario 1 - Profit Surplus Every day

def calculate_profit_loss(data):
    for day in data:
        daily_net_profit = day[4] - data[day[0] - 1][4] if day[0] > 0 else day[4]
        if daily_net_profit >= 0:
            print(f"[PROFIT SURPLUS] DAY: {day[0]}, AMOUNT: USD {daily_net_profit}")
        else:
            print(f"[PROFIT DEFICIT] DAY: {day[0]}, AMOUNT: USD {-daily_net_profit}")

def find_highest_profit_surplus(data):
    highest_profit = 0
    highest_day = -1

    for day in data:
        daily_net_profit = day[4] - data[day[0] - 1][4]
        if daily_net_profit > 0 and daily_net_profit > highest_profit:
            highest_profit = daily_net_profit
            highest_day = day[0]

    return highest_profit, highest_day

# Call the functions for each scenario and highest net profit surplus
highest_profit_surplus, highest_profit_surplus_day = find_highest_profit_surplus(profit_and_loss)

# This line changes the directory from the operating system back to the original.
os.chdir(original_working_dir)

