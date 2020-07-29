# 0 to 36 wheel roulette
import random
import time
import math


def convert_percent(percent):
    return (1 - percent) * 100


lose_chance = 19 / 36
starting_cash = int(input("Starting cash: "))
profit = int(input("How much profit: "))
n_roll = math.log2((5 + starting_cash) / 5)
n_roll = math.floor(n_roll)

percent_loss = lose_chance ** n_roll
total_wins = profit / 5
profit_percent = convert_percent(percent_loss * total_wins)
print(f"{profit_percent}%")