import os
from pathlib import Path
import csv

original_working_dir= os.getcwd()

# Set the current working directory to the folder containing the CSV file
csv_folder = os.path.join(os.getcwd(), "csv_reports")
os.chdir(csv_folder)

# Now you can open and read the CSV file
csv_file = "Profit_And_Loss.csv"

with open(csv_file, mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    profit_and_loss = []

    for row in reader:
        profit_and_loss.append([int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4])])

# Calculate Profit and Loss for Scenario 1 - Profit Surplus Everyday
def calculate_profit_loss_scenario1(data):
    is_profit_surplus = True
    for i in range(len(data)):
        profit = data[i][2]
        if profit <= 0:
            is_profit_surplus = False
            break

    if is_profit_surplus:
        
        for i in range(len(data)):
            profit = data[i][2]
            print(f"DAY: {data[i][0]}, AMOUNT: {profit}")
            if i > 0 and data[i][4] > data[i - 1][4]:
                print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        
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
