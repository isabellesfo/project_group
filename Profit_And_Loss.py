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

# This function calculates the daily net profit and identifies whether it's a surplus or a deficit.
# It also takes a list of data as input, where each entry contains day information and net profit value.
def calculate_profit_loss(data):
    for day in data:
# This code calculates the daily net profit by subtracting the previous day's net profit from the current day's net profit.
        daily_net_profit = day[4] - data[day[0] - 1][4] if day[0] > 0 else day[4]
        
# This code checks if the daily net profit is positive (surplus) or negative (deficit) and print accordingly.
        if daily_net_profit >= 0:
            print(f"[PROFIT SURPLUS] DAY: {day[0]}, AMOUNT: USD {daily_net_profit}")
        else:
            print(f"[PROFIT DEFICIT] DAY: {day[0]}, AMOUNT: USD {-daily_net_profit}")

# This function finds the highest net profit surplus among the given data.
# It also takes a list of data as input, similar to the calculate_profit_loss function.
def find_highest_profit_surplus(data):
# This code initialise the highest profit to 0.
    highest_profit = 0  

# This code initialise the day with the highest profit surplus to -1.   
    highest_day = -1       

# This code iterate through each day's data to find the highest profit surplus.
    for day in data:

# This code calculates the daily net profit by subtracting the previous day's net profit from the current day's net profit.
        daily_net_profit = day[4] - data[day[0] - 1][4]
        
# This code checks if the daily net profit is positive and higher than the current highest profit.
# If it is it updates the highest profit and the corresponding day.
        if daily_net_profit > 0 and daily_net_profit > highest_profit:
            highest_profit = daily_net_profit
            highest_day = day[0]

# This code returns the highest profit surplus and the corresponding day.
    return highest_profit, highest_day

# This code calls the find_highest_profit_surplus function with the profit_and_loss data to find the highest profit surplus and its corresponding day.
highest_profit_surplus, highest_profit_surplus_day = find_highest_profit_surplus(profit_and_loss)

# This line changes the directory from the operating system back to the original.
os.chdir(original_working_dir)
