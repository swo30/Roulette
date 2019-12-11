import random

cornerlist = {1,2,4,5}
red = {1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36}
blacklist = {2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35}
green = 0
evenlist = {2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36}
odd = {1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35}
gameswon = 0

def main():
    gameswon = 0
    totalearning = 0
    amountofgames = 10      #####

    for gamecount in range (1,amountofgames+1,1):
        gamebalance = game(gamecount)
        totalearning += gamebalance
        if gamebalance > 0:
            gameswon +=1
    print("Games won: {}/{}".format(gameswon, amountofgames))
    print("Win rate " + str(int(float(gameswon)/amountofgames *100)) + "%")
    print("Average earning per game {}$".format(int(totalearning/amountofgames)))
    print("Total earnings {}$".format(int(totalearning)))

def game(gamecount):
    global balance
    global rollcount
    global bet
    global resetbet

    bet = 5                 #####
    resetbet = 5            #####
    amountofrolls = 20      ##### 40 ish min
    wallet = 200            #####
    balance = 0
    
    actualmaxbet = maxbet(bet, wallet)
    print("With {}$, the max bet is {}$\n".format(wallet, actualmaxbet))

    for rollcount in range (0,amountofrolls,1):
        if bet > actualmaxbet: ####total of 155 if 80 max bet
            print("GAME {} STOPPED AFTER {} TURNS\n".format(gamecount, rollcount))
            break
        else:
            result = roll()

    print("Game {} Balance: {}$".format(gamecount, balance))
    print("=================================================")

    return(balance)

def maxbet(bet, wallet):
    while wallet > 0:
        wallet -= bet
        actualmaxbet = bet
        if wallet < bet:
            break
        bet *= 2

    return(actualmaxbet)

def roll():
    global rollcount
    global bet
    global balance
    global LOB
    global resetbet

    landon = random.randint(0, 36) #####36 for europe

    balance -= bet
    prevbet = bet
    if landon in evenlist:
        balance += int(bet)*2
        bet = resetbet
    else:
        bet *= 2
        
    print("@roll {}, bet was {}$, land-on = {}, \n new balance = {}$".format(rollcount+1, prevbet, landon, balance))
    return(landon)
    
main()
