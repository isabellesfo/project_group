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
def calculate_profit_loss_scenario1(data):
    is_profit_surplus = True
    highest_net_profit_surplus = 0  # Initialize with zero

    for i in range(1, len(data)):
        net_profit_increase = data[i][4] - data[i - 1][4]  # Calculate increase in net profit from the previous day
        if net_profit_increase <= 0:
            is_profit_surplus = False
            break

        if net_profit_increase > highest_net_profit_surplus:
            highest_net_profit_surplus = net_profit_increase

    if is_profit_surplus:
  
        for i in range(len(data)):
            net_profit = data[i][4]
            print(f"DAY: {data[i][0]}, AMOUNT: {net_profit}")
            if i > 0 and data[i][4] > data[i - 1][4]:
                print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

        print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {data[-1][0]}, AMOUNT: USD{highest_net_profit_surplus}")

# Calculate Profit and Loss for Scenario 2 - Constant Profit Deficit Every day
def calculate_profit_loss_scenario2(data):
    is_profit_deficit = True
    for day in range(len(data)):
        net_profit = data[day][4]
        if net_profit >= 0:
            is_profit_deficit = False
            break

    if is_profit_deficit:

        for day in range(len(data)):
            deficit = data[day][4] * -1
            print(f"DAY: {data[day][0]}, AMOUNT: {deficit}")

# Calculate Profit and Loss for Scenario 3 - Fluctuation between Profit Surplus and Profit Deficit
def calculate_profit_loss_scenario3(data):
    has_profit_surplus = False
    has_profit_deficit = False

    for day in range(len(data)):
        net_profit = data[day][4]
        if net_profit > 0:
            has_profit_surplus = True
        elif net_profit < 0:
            has_profit_deficit = True

    if has_profit_surplus and has_profit_deficit:

        for day in range(len(data)):
            net_profit = data[day][4]
            if net_profit > 0:
                print(f"[PROFIT SURPLUS] DAY: {data[day][0]}, AMOUNT: USD{net_profit}")
            elif net_profit < 0:
                deficit = net_profit * -1
                print(f"[PROFIT DEFICIT] DAY: {data[day][0]}, AMOUNT: USD{deficit}")

# Find Highest Net Profit Surplus
def find_highest_net_profit_surplus(data):
    highest_net_profit_surplus = 0  # Initialize with zero
    for day in range(1, len(data)):
        net_profit_surplus = data[day][4] - data[day - 1][4]  # Calculate net profit surplus (today's net profit - yesterday's net profit)
        if net_profit_surplus > highest_net_profit_surplus:
            highest_net_profit_surplus = net_profit_surplus
    return highest_net_profit_surplus

# Calling the functions for each scenario and highest net profit surplus

highest_net_profit_surplus = find_highest_net_profit_surplus(profit_and_loss)

# This line changes the directory from the operating system back to the original.
os.chdir(original_working_dir)
