import random

simulations = 100000
switch = True
wins = 0
print(f"Switch is {switch}")

for i in range(1, simulations):
    doors = [1,2,3]
    prize = random.randint(1,3) #doors[random.randint(1,3) - 1]
    doors.remove(prize)
    goat1,goat2 = doors

    pick = random.randint(1,3)
    if pick == goat1:
        doors.remove(goat2)
    else:
        doors.remove(goat1) #picked goat2 or prize

    if switch:
        if pick == doors[0]:
            pick = prize

        elif pick == prize:
            pick = doors[0]

    if pick == prize:
        wins += 1

if switch:
    print(f"You have a {100*wins/simulations}% chance of winning by switching")
else:
    print(f"You have a {100*wins/simulations}% chance of winning by not switching")
