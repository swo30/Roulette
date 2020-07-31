# 0 to 36 wheel roulette
import random
import time
import math

def fill_starting_array(arr):
    if not arr:
        arr.append(5)
    while len(arr) < 6:
        arr.append(5 + arr[-1] * 2)
    return arr

def print_property(str,property):
    print(f"{str}: {property}")

lose_chance = 13 / 37
starting_cash_array = []
starting_cash_array = fill_starting_array(starting_cash_array)

starting_cash = int(input("Starting cash: "))
profit = int(input("How much profit: "))
n_roll = math.log2((starting_cash) / 5)
n_roll = math.floor(n_roll) - 1

percent_loss = lose_chance ** n_roll #chance of losing all money
total_wins = math.ceil(profit / 5)
profit_percent = ((1-percent_loss) ** total_wins)*100
print(f"profit_percent: {profit_percent}%")
