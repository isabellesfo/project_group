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

# This line finds the highest net profit surplus from "data".
# The max() function is used to find the maximum value based on the fifth element of the sublist in "data" and the amount is stored in the "highest_net_profit_surplus" variable.
        highest_net_profit_surplus = max(data, key=lambda x: x[4])[4]
        print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {data[-1][0]}, AMOUNT: {highest_net_profit_surplus}")

# This line takes the "data" as input.
def calculate_profit_loss_scenario2(data):

# This function initialises a boolean variable "is_profit_deficit" and sets it to "True". This variable will be used to track if theres a deficit or not.
    is_profit_deficit = True

# This line of code is a loop that iterates over the "data" using the indices and extracts the profit or loss amount for each day and stores it in the "profit" variable.
    for i in range(len(data)):
        profit = data[i][2]

# This line of code checks if "profit" is greater than or equal to zero. 
# If there is a positive profit on that day, it sets "is_profit_decifit" to "False"
        if profit >= 0:
            is_profit_deficit = False
            break

# This line of code checks the value of "is_profit_deficit", if it is true, all the days in "data" would have a deficit.
    if is_profit_deficit:
        
# This line of code executes only if "is_profit_deficit" is true.
# This line calculates the deficit amount for each day.
        for i in range(len(data)):
            deficit = data[i][2] * -1
            print(f"DAY: {data[i][0]}, AMOUNT: {deficit}")

# This line takes the "data" as input.
def calculate_profit_loss_scenario3(data):

# This line of code initialises a boolean variable "has_profit_surplus" and sets it to "False". This function tracks if there is any day with a positive profit surplus.
    has_profit_surplus = False

# This line of code initialises a boolean variable "has_profit_deficit" and sets it to "False". This function tracks if there is any day with a negative profit deficit.
    has_profit_deficit = False

    for i in range(len(data)):
        profit = data[i][2]

# This line of code checks if "profit" is greater than zero, if it is, it set "has_profit_surplus" to "True".
        if profit > 0:
            has_profit_surplus = True

# This line of code checks if "profit" is smaller than zero, if it is, it set "has_profit_deficit" to "True".
        elif profit < 0:
            has_profit_deficit = True

# This code checks the values of "has_profit_surplus" and "has_profit_deficit". If both of them are True, it means there are days with both positive profit surplus and negative profit deficit.
    if has_profit_surplus and has_profit_deficit:
        
        for i in range(len(data)):
            profit = data[i][2]

# This line of code checks if "profit" is greater than zero, if it is, it prints the statement "[PROFIT SURPLUS] DAY: {data[i][0]}, AMOUNT: USD {profit}".
            if profit > 0:
                print(f"[PROFIT SURPLUS] DAY: {data[i][0]}, AMOUNT: USD {profit}")

# This line of code checks if "profit" is smaller than zero, if it is, calculates the deficit amount by multiplying the profit/loss amount by -1 and prints the statement ""[PROFIT DEFICIT] DAY: {data[i][0]}, AMOUNT: USD {deficit}".
            elif profit < 0:
                deficit = data[i][2] * -1
                print(f"[PROFIT DEFICIT] DAY: {data[i][0]}, AMOUNT: USD {deficit}")

# This line takes the "data" as input.
def find_highest_net_profit_surplus(data):

# This line of code initialises a variable "highest_net_profit_surplus" and sets it to the net profit of the first day in "data".
# This value serves as the initial highest net profit surplus. 
    highest_net_profit_surplus = data[0][4]
    for i in range(1, len(data)):

# This line of code extracts the net profit for the current and stores it in the variable "net_profit".
        net_profit = data[i][4]

# This line of code checks if the "net_profit" for the current day is greater than the "highest_net_profit_surplus" and updates the "highest_net_profit_surplus" variable with a new value.
        if net_profit > highest_net_profit_surplus:
            highest_net_profit_surplus = net_profit
    return highest_net_profit_surplus

# This line changes the directory from the operating system back to the original.
os.chdir(original_working_dir)
