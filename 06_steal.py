import random


STARTING_BALANCE = 100

balance = STARTING_BALANCE

steal_up = 0


for item in range (0,10) :
    chosen_num = random.randint(1, 100)
    if 1 <= chosen_num <= 50 + steal_up :
        chosen = "You stole money"
        balance = 1.4 * balance
    elif 51 + steal_up <= chosen_num <= 100 :
        chosen = "You got caught"
        balance = 0.7 * balance

    
    print("You got a {}.  Your balance is ${:.2f} " .format(chosen, balance))
    
