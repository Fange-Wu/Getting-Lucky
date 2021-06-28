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
    if 1 <= chosen_num <= 50 :
        chosen = "You stole money"
        balance += 4
    
    # if the random # is between 6 and 46
    # user will get donkey *minus 1$ from balance
    elif 51 <= chosen_num <= 100 :
        chosen = "You got caught"

    
    print("You got a {}.  Your balance is ${:.2f} " .format(chosen, balance))
    
print()
print()
print("Starting Balance: ${:.2f}" .format(STARTING_BALANCE))
print("Final Balance: ${:.2f}" .format(balance))