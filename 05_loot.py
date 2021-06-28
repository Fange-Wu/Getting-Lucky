import random
tokens = ["win", "win", "win", "win","lose"]
STARTING_BALANCE = 0

balance = STARTING_BALANCE


# Testing loop to genereate 20 tokens
for item in range (0,100) :
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    
print()
print("Starting Balance: ${:.2f}" .format(STARTING_BALANCE))
print("Final Balance: ${:.2f}" .format(balance))