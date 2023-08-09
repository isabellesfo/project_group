#These lines imports the respective dictionaries into the main folder.
from overheads import overhead_data, find_highest_overhead
from cash_on_hand import cash_data, calculate_cash_surplus_deficit
from profit_and_loss import (
    profit_and_loss,
    calculate_profit_loss,
    find_highest_profit_surplus,
)

# This lines will call the function from "overheads.py"
highest_overhead = find_highest_overhead(overhead_data)
print(f"[HIGHEST OVERHEAD] {highest_overhead[0]}: {highest_overhead[1]}%")

# This line will call the function from "cash_on_hand.py"
calculate_cash_surplus_deficit(cash_data)
largest_increment = 0
largest_increment_day = None
largest_deficit = 0
largest_deficit_day = None

for i in range(1, len(cash_data)):   
    current_cash = cash_data[i][1]
    previous_cash = cash_data[i - 1][1]
    increment = current_cash - previous_cash

    if increment > largest_increment:
            largest_increment = increment
            largest_increment_day = cash_data[i][0]

    if increment < largest_deficit:
            largest_deficit = increment
            largest_deficit_day = cash_data[i][0]

# This lines will call the functions from "profit_and_loss.py"
calculate_profit_loss(profit_and_loss)

# This line will call the function "find_highest_net_profit_surplus" and passes the variable "profit_and_loss" as an argument. 
# The function is expected to calculate and return the highest net profit surplus. The returned value will be assigned to the variable "highest_net_profit_surplus".

highest_profit_surplus, highest_profit_surplus_day = find_highest_profit_surplus(profit_and_loss)

# This accesses the first element of the last element in "profit_and_loss" and prints the messgae which includes the day from the "profit_and_loss" data and the value of the "highest_net_profit_surplus" variable.
print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_profit_surplus_day}, AMOUNT: USD {highest_profit_surplus}")

with open("summary.txt", "w") as file:
        file.write(f"[HIGHEST OVERHEAD] {highest_overhead[0]}: {highest_overhead[1]}%\n")
        file.write(f"[LARGEST INCREMENT] DAY: {largest_increment_day}, AMOUNT: USD {largest_increment}\n")
        file.write(f"[LARGEST DEFICIT] DAY: {largest_deficit_day}, AMOUNT: USD {-largest_deficit}\n")
        file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_profit_surplus_day}, AMOUNT: USD {highest_profit_surplus}")