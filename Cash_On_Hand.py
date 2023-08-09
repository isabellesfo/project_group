# This function imports the relevant functions to help import the csv file from the folder "csv_reports".
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

# This line initialize variables to find the largest increment and largest deficit, along with their corresponding days.
    largest_increment = 0
    largest_increment_day = None
    largest_deficit = 0
    largest_deficit_day = None

# This line iterate through the data starting from the second element.
    for i in range(1, len(data)):

 # This line assigns the data at index i to current_cash.
        current_cash = data[i][1]

# This line assigns the data at index i -1 to previous_cash.
        previous_cash = data[i - 1][1]

# This line calculates the increment in cash by taking the current_cash minusing the previous_cash.
        increment = current_cash - previous_cash

# This line compares increment with the largest_increment value and if it's larger, it will update the variables.
        if increment > largest_increment:
            largest_increment = increment
            largest_increment_day = data[i][0]

# This line compares increment with the largest_deficit value and if it's smaller, it will update the variables.
        if increment < largest_deficit:
            largest_deficit = increment
            largest_deficit_day = data[i][0]

# This line checks if current_cash is greater than the previous_cash.
        if current_cash > previous_cash:
            print(f"[CASH SURPLUS] DAY: {data[i][0]}, AMOUNT: USD {increment}")

# This line checks if the current_cash is less than the previous_cash.
        elif current_cash < previous_cash:
            print(f"[CASH DEFICIT] DAY: {data[i][0]}, AMOUNT: USD {-increment}")

# This codes only runs if largest_increment_day or largest_deficit_day is not None and it will print the largest increment and largest deficit along with their corresponding days.
    if largest_increment_day is not None:
        print(f"[LARGEST INCREMENT] DAY: {largest_increment_day}, AMOUNT: USD {largest_increment}")

    if largest_deficit_day is not None:
        print(f"[LARGEST DEFICIT] DAY: {largest_deficit_day}, AMOUNT: USD {-largest_deficit}")
    

# This line changes the directory from the operating system back to the original.
os.chdir(original_working_dir)
