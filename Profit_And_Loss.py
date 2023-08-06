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
def calculate_profit_loss_scenario1(data):

# This line initialises a boolean variable 'is_profit_surplus' and sets it to "True", which tracks whether there is a profit surplus until proven otherwise. 
    is_profit_surplus = True

# This line is a loop that runs for each element in the range in "data".
    for i in range(len(data)):

# This line takes the third element from "i" in the "data" list and assigns it to the variable "profit".
        profit = data[i][2]

# This line of code checks whether the "profit" value is less than or equal to zero and if the condition is true , the profit will either be zero or negative, meaning no profit surplus. 
# If the "profit" is less than or equal to zero, the 'is_profit_surplus' is set to false, indicating that there is no profit surplus. 
# 'break' is used to exit the loop immediately.
        if profit <= 0:
            is_profit_surplus = False
            break

# This line of code checks if the variable "is_profit_surplus" is "True". If it is true, the code inside the block will be executed. 
    if is_profit_surplus:

# This line of code is a loop that iterates over the indices of the "data" list
        for i in range(len(data)):

# This line of code assigns the variable "profit" to the value of the third element in "data" at the index "i".
            profit = data[i][2]

# This line prints the day and the corresponding profit amount for each element in the "data" list. 
# The day is represented by the first element in "data" at the index "i" and the profit amount is stored in the variable "profit".
            print(f"DAY: {data[i][0]}, AMOUNT: {profit}")

# This line checks if the current day's net profit is greater than the net profit of the previous day. If it is true it will print the messgage below.
            if i > 0 and data[i][4] > data[i - 1][4]:
                print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

#
        highest_net_profit_surplus = max(data, key=lambda x: x[4])[4]
        print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {data[-1][0]}, AMOUNT: {highest_net_profit_surplus}")

# Calculate Profit and Loss for Scenario 2 - Constant Profit Deficit Everyday
def calculate_profit_loss_scenario2(data):
    is_profit_deficit = True
    for i in range(len(data)):
        profit = data[i][2]
        if profit >= 0:
            is_profit_deficit = False
            break

    if is_profit_deficit:
        
        for i in range(len(data)):
            deficit = data[i][2] * -1
            print(f"DAY: {data[i][0]}, AMOUNT: {deficit}")

# Calculate Profit and Loss for Scenario 3 - Fluctuation between Profit Surplus and Profit Deficit
def calculate_profit_loss_scenario3(data):
    has_profit_surplus = False
    has_profit_deficit = False

    for i in range(len(data)):
        profit = data[i][2]
        if profit > 0:
            has_profit_surplus = True
        elif profit < 0:
            has_profit_deficit = True

    if has_profit_surplus and has_profit_deficit:
        
        for i in range(len(data)):
            profit = data[i][2]
            if profit > 0:
                print(f"[PROFIT SURPLUS] DAY: {data[i][0]}, AMOUNT: USD {profit}")
            elif profit < 0:
                deficit = data[i][2] * -1
                print(f"[PROFIT DEFICIT] DAY: {data[i][0]}, AMOUNT: USD {deficit}")

# Find Highest Net Profit Surplus without using abs()
def find_highest_net_profit_surplus(data):
    highest_net_profit_surplus = data[0][4]
    for i in range(1, len(data)):
        net_profit = data[i][4]
        if net_profit > highest_net_profit_surplus:
            highest_net_profit_surplus = net_profit
    return highest_net_profit_surplus

os.chdir(original_working_dir)
