# This function imports the relevant functions to help import the csv file from the folder "csv_reports".
import os
from pathlib import Path
import csv

# This stores the current working directory in the variable.
original_working_dir= os.getcwd()

# This sets the current working directory to the folder containing the CSV file.
csv_folder= os.path.join(os.getcwd(), "csv_reports")
os.chdir(csv_folder)

# The variable that stores the name of the csv file, "Cash_On_Hand.csv" that the code will read.
csv_file= "Cash_On_Hand.csv"

with open(csv_file, mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    cash_data = []

    for row in reader:
        cash_data.append([int(row[0]), float(row[1])])

# Calculate Cash Surplus or Cash Deficit
def calculate_cash_surplus_deficit(data):
    has_cash_surplus = False
    has_cash_deficit = False

    for i in range(1, len(data)):
        current_cash = data[i][1]
        previous_cash = data[i - 1][1]

        if current_cash > previous_cash:
            has_cash_surplus = True
            print(f"[CASH SURPLUS] DAY: {data[i][0]}, AMOUNT: {current_cash - previous_cash}")

        elif current_cash < previous_cash:
            has_cash_deficit = True
            print(f"[CASH DEFICIT] DAY: {data[i][0]}, AMOUNT: {previous_cash - current_cash}")

os.chdir(original_working_dir)
