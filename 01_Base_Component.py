import random
# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is between 10-30"

        if response != "":
            try:
                response = int(response)

                if response < 10 or response > 30:
                    print(round_error)
                    continue
            
            except ValueError:
                print(round_error)
                continue
        
        return response

def valid_checker(userchoice):
    valid = False
    while not valid:
        response = input(userchoice).lower()
        if response not in ('loot', 'steal', 'job', 'shop', 'xxx'):
            print("")
            print("ERROR Please choose Loot, Steal, Job, Shop or XXX to quit ")
        else:
            print("You chose {}".format(response))
            userchoice == response
            return response
            break

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If yes program continue
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no display instructions
        elif response == "no" or response == "n":
            response = "no"
            return response

        # ask user to enter a valid answer
        else: 
            print("Please answer yes / no ")

def instructions() :
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    instructions()


play = True
while play:
    rounds_played = 0
    rounds = check_rounds()
    end_game = "no"
    tokens = ["win", "win", "win", "win","lose"]
    STARTING_BALANCE = 0
    upgrade = 0
    win = 10 + upgrade
    balance = STARTING_BALANCE
    goal = rounds * 10
    steal_up = 0
    while balance < goal:
        if balance >= goal :
                print("Congratulations! You Won!")
                break
        if rounds_played >= rounds:
                print("You lost you didn't meet the money goal!")
                break
        print()
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        print("Money Goal: ${}".format(goal))
        print("Current Balance: ${:.2f}".format(balance))
        choice = valid_checker("Please choose Loot, Steal, Job, Shop or XXX to quit ")
        
        if choice == "xxx":
            play = False
            break

        if choice == "shop":
            print("Welcome to the store!")
            while True:
                print("Your current balance ${}".format(balance))
                print("You can buy:")
                price_list = {'loot':10, 'steal':15, 'job':20}
                for key in price_list:
                    item = key
                    price = price_list[key]
                    print("{} upgrade | cost: ${}".format(item, price))
                price_list = {'loot':10, 'steal':15, 'job':20}

                buy = input("What do you want to buy? ")
                if buy == "exit":
                    break
                elif buy in price_list:
                    price = price_list[buy]
                    if balance > price:
                        balance -= price
                        print("You bought: ", buy)
                        print("It costed: $", price)
                        if buy == "loot":
                            loot_up += 2
                        elif buy == "steal":
                            steal_up += 2
                        if buy == "job":
                            job_up += 2
            
                    elif balance < price:
                        print("You don't have enough money")
                        missing = balance - price
                        print("You are missing $", missing)

                else:
                    print("Please choose something from list")
        elif choice == "loot":
            chosen = random.choice(tokens)

                # Adjust balance
            if chosen == "win":
                balance += win
                print("You looted and found ${} \nbalance = ${}".format(win, balance))
            
            else:
                print("You didn't find anything")
            rounds_played += 1
        
        elif choice == "steal":
            chosen_num = random.randint(1, 100)
            if 1 <= chosen_num <= 50 + steal_up :
                chosen = "You stole money."
                balance = 1.4 * balance
            elif 51 + steal_up <= chosen_num <= 100 :
                chosen = "You got caught."
                balance = 0.7 * balance
            print("{}.  Your balance is ${:.2f} " .format(chosen, balance))
        
            rounds_played += 1
    
        elif choice == "job":
            operation = random.randint(1,3)
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)

            if operation == 1:
                question = int(input("What is " + str(num1) + "+" + str(num2) + ": "))
                answer = num1 + num2
                if question == answer:
                    print("You got it right")
                    balance += 8
                else:
                    print("You got it wrong")

            elif operation == 2:
                question = int(input("What is " + str(num1) + "-" + str(num2) + ": "))
                answer = num1 - num2
                if question == answer:
                    print("You got it right")
                    balance += 8
                else:
                    print("You got it wrong")

            elif operation == 3:
                question = int(input("What is " + str(num1) + "x" + str(num2) + ": "))
                answer = num1 * num2
                if question == answer:
                    print("You got it right")
                    balance += 8
                else:
                    print("You got it wrong")
            rounds_played += 1
            print("balance = ${}".format(balance))

    if play == True:
        again= yes_no("Do you want to play again, type yes or no ")
        if again == "no":
            play = False
print("Thank you for playing")