# main.py
#imports the respective dictionaries into the main folder
from overheads import overhead_data, find_highest_overhead
from cash_on_hand import cash_data, calculate_cash_surplus_deficit
from profit_loss import (
    profit_and_loss,
    calculate_profit_loss_scenario2,
    calculate_profit_loss_scenario3,
    find_highest_net_profit_surplus,
)

# Call the function from "overheads.py"
highest_overhead = find_highest_overhead(overhead_data)
print(f"[HIGHEST OVERHEAD] {highest_overhead[0]}: {highest_overhead[1]}%")

# Call the function from "cash_on_hand.py"
calculate_cash_surplus_deficit(cash_data)

# Call the functions from "profit_and_loss.py"
calculate_profit_loss_scenario2(profit_and_loss)
calculate_profit_loss_scenario3(profit_and_loss)

highest_net_profit_surplus = find_highest_net_profit_surplus(profit_and_loss)
print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {profit_and_loss[-1][0]}, AMOUNT: USD {highest_net_profit_surplus}")