# 0 to 36 wheel roulette
import random
import time
import math
import matplotlib.pyplot as plt

def average(arr):
    sum = 0
    for element in arr:
        sum+=element
    return sum/len(arr)

xaxis = []
top_earnings = []
max_cash_index = []
lose_chance = 13 / 37
simulations = 1000
starting_cash = 80
for i in range(simulations):
    top_earnings.append(0)
    max_cash_index.append(0)

for sim in range(simulations):
    wallet = starting_cash
    loss_in_a_row = 0; wins = 0;
    games = 0
    
    while True:
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
                
        if top_earnings[sim] < wallet:
            top_earnings[sim] = wallet
            max_cash_index[sim] = games
    

#plt.plot(xaxis)
#plt.ylabel('some numbers')
#plt.show()
print(f"Top earnings average: {average(top_earnings)}")
print(f"Max cash index average: {average(max_cash_index)}")
print(f"Profit is: {int(average(top_earnings)-starting_cash)}")