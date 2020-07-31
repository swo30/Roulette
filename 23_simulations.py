# 0 to 36 wheel roulette
import random
import time
import math
import matplotlib.pyplot as plt
from matplotlib import colors

def average(arr):
    sum = 0
    for element in arr:
        sum+=element
    return int(sum/len(arr))

def normal_plot(simulations,starting_cash,top_earnings):
    plt.plot(top_earnings)
    plt.plot([1, simulations], [starting_cash, starting_cash])
    plt.xlabel('Simulation')
    plt.ylabel('Top money')
    plt.show()

def histogram(d):
    n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Top Money')
    plt.ylabel('Frequency')
    plt.title('Roulette 2/3 strat')
    # plt.text(200, 100, r'$\mu=15, b=3$')
    plt.show()

top_earnings = []
max_cash_index = []
simulations = 100000
starting_cash = 80
for i in range(simulations):
    top_earnings.append(0)
    max_cash_index.append(0)

for sim in range(simulations):
    wallet = starting_cash
    loss_in_a_row = 0; wins = 0;
    games = 0

    while True:
        if top_earnings[sim] < wallet:
            top_earnings[sim] = wallet
            max_cash_index[sim] = games

        bet = 10*(2**loss_in_a_row)
        #print(f"You have: {wallet}$ left")
        #print(f"Trying to bet: {bet}$")
        xaxis.append(wallet)
        wallet = wallet - bet
        if wallet < 0:
            #print("Don't have enough to continue.")
            break
        else:
            games += 1
            number = random.randint(0, 36)
            if number > 24 or number == 0:
                #print("You lost")
                loss_in_a_row += 1
            else:
                #print("You won")
                wins += 1
                loss_in_a_row = 0
                wallet += bet*(3/2)


print(f"Top earnings average: {average(top_earnings)}")
print(f"Max cash index average: {average(max_cash_index)}")
print(f"Profit is: {average(top_earnings)-starting_cash}")

profit_count = 0
profit_2_times = 0
lost_all = 0
for cash in top_earnings:
    profit = cash - starting_cash
    if profit <= 0:
        lost_all += 1
    else:
        profit_count += 1

    if profit >= starting_cash:
        profit_2_times += 1

print(f"You made a profit: {profit_count} times out of {simulations}")
print(f"You made 2x starting cash: {profit_2_times} times out of {simulations}")
print(f"You lost all your starting money: {lost_all} times out of {simulations}")

# normal_plot(simulations,starting_cash,top_earnings)
# histogram(top_earnings)

