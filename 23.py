# 0 to 36 wheel roulette
import random
import time
import math

def fill_starting_array(arr):
    if not arr:
        arr.append(10)
    while len(arr) < 6:
        arr.append(10 + arr[-1] * 2)
    return arr

lose_chance = 13 / 37
starting_cash_array = []
starting_cash_array = fill_starting_array(starting_cash_array)
starting_cash_array = [75]
profit = 20
print(starting_cash_array)
print(f"For {profit}$ of profit.")

for starting_cash in starting_cash_array:
    # starting_cash = int(input("Starting cash: "))
    # profit = int(input("How much profit: "))
    n_roll = math.log2((10 + starting_cash) / 10)
    n_roll = math.floor(n_roll)

    percent_loss = lose_chance ** n_roll #chance of losing all money
    total_wins = math.ceil(profit / 5)
    profit_percent = ((1-percent_loss) ** total_wins)*100
    print(f"Profit percent: {profit_percent}%")
