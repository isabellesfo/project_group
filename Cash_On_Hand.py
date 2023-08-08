# This function imports the relevant functions to help import the csv file from the folder "csv_reports".
import os
from pathlib import Path
import csv

original_working_dir= os.getcwd()

# This lines sets the current working directory to the folder containing the CSV file. 
csv_folder = os.path.join(os.getcwd(), "csv_reports")
os.chdir(csv_folder)

# This line opens and reads the CSV file.
csv_file = "Cash_On_Hand.csv"

# This opens and reads the csv file.
with open(csv_file, mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

# This skips the header row as it contains column names that are not needed. 
    next(reader)

# This assigns an empty list to the variable overhead_data. 
    cash_data = []

# This is a loop that will execute the code for each row of data in reader. 
    for row in reader:

# This appends the list for the code and creates a new list with a converted integer and float value
        cash_data.append([int(row[0]), float(row[1])])

# This line of code calculates Cash Surplus or Cash Deficit and Find Largest Increment or Deficit
def calculate_cash_surplus_deficit(data):
    largest_increment = 0
    largest_increment_day = None
    largest_deficit = 0
    largest_deficit_day = None

    for i in range(1, len(data)):
        current_cash = data[i][1]
        previous_cash = data[i - 1][1]
        increment = current_cash - previous_cash

        if increment > largest_increment:
            largest_increment = increment
            largest_increment_day = data[i][0]

        if increment < largest_deficit:
            largest_deficit = increment
            largest_deficit_day = data[i][0]

        if current_cash > previous_cash:
            print(f"[CASH SURPLUS] DAY: {data[i][0]}, AMOUNT: USD{increment}")
        elif current_cash < previous_cash:
            print(f"[CASH DEFICIT] DAY: {data[i][0]}, AMOUNT: USD{-increment}")

    if largest_increment_day is not None:
        print(f"[LARGEST INCREMENT] DAY: {largest_increment_day}, AMOUNT: USD{largest_increment}")

    if largest_deficit_day is not None:
        print(f"[LARGEST DEFICIT] DAY: {largest_deficit_day}, AMOUNT: USD{-largest_deficit}")
    

# This line changes the directory from the operating system back to the original.
os.chdir(original_working_dir)
