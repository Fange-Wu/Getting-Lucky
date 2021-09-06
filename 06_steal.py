import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE

steal_up = 0

# Testing loop to genereate 20 tokens
for item in range (0,10) :
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5 
    # user will get unicorn *add 4$ to balance
    if 1 <= chosen_num <= 50 + steal_up :
        chosen = "You stole money"
        balance = 1.4 * balance
    
    # if the random # is between 6 and 46
    # user will get donkey *minus 1$ from balance
    elif 51 + steal_up <= chosen_num <= 100 :
        chosen = "You got caught"
        balance = 0.7 * balance

    
    print("You got a {}.  Your balance is ${:.2f} " .format(chosen, balance))
    
