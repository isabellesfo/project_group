# This function imports the relevant functions to help import the csv file from the folder "csv_reports".
#import os
from pathlib import Path
import csv

# This stores the current working directory in the variable.
original_working_dir= os.getcwd()

# This sets the current working directory to the folder containing the CSV file.
csv_folder= os.path.join(os.getcwd(), "csv_reports")
os.chdir(csv_folder)

# The variable that stores the name of the csv file, "Cash_On_Hand.csv" that the code will read.
csv_file= "Cash_On_Hand.csv"

# This opens and reads the csv file.
with open(csv_file, mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

# This skips the header row as it contains column names that are not needed. 
    next(reader)

# This assigns an empty list to the variable cash_data. 
    cash_data = []

# This is a loop that will execute the code for each row of data in reader. 
    for row in reader:

# This appends the list for the code and creates a new list with a converted integer and float value
        cash_data.append([int(row[0]), float(row[1])])

# This helps defines the function "calculate_cash_surplus_deficit" with the parameter "data".
def calculate_cash_surplus_deficit(data):

# This lines initialises the variable with the value "False", assuming there is no cash until proven later on in the code.
    has_cash_surplus = False
    has_cash_deficit = False

# This is a loop that will execute the code for the data in the range. 
    for i in range(1, len(data)):

# This line assigns the value of the second elemnt of the 'i' in the "data" list to the variable "current_cash".
        current_cash = data[i][1]
        
# This line assigns the value of the second elemnt of the 'i-i' in the "data" list to the variable "previous_cash".
        previous_cash = data[i - 1][1]

# This line checks if the "current_cash" value is greater than the "previous_cash" and if it is "True", the code under this"if" function will run.
        if current_cash > previous_cash:
            has_cash_surplus = True
            print(f"[CASH SURPLUS] DAY: {data[i][0]}, AMOUNT: {current_cash - previous_cash}")

# This line checks if the "current_cash" value is smaller than the "previous_cash" and if it is "True", the code under this "if" function will run.
        elif current_cash < previous_cash:
            has_cash_deficit = True
            print(f"[CASH DEFICIT] DAY: {data[i][0]}, AMOUNT: {previous_cash - current_cash}")

# This line changes the directory from the operating system back to the original.
os.chdir(original_working_dir)