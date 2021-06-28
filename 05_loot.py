import random
tokens = ["win", "win", "win", "win","lose"]
STARTING_BALANCE = 0
upgrade = 0
win = 8 + upgrade
balance = STARTING_BALANCE


# Testing loop to genereate 20 tokens
for item in range (0,10) :
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "win":
        balance += win
        print("You looted and gained ${} \n balance = ${}".format(win, balance))
 
    else:
        print("You didn't get anything")

    
print()
print("Starting Balance: ${:.2f}" .format(STARTING_BALANCE))
print("Final Balance: ${:.2f}" .format(balance))