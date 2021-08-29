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
    print("Choose number of rounds 10-30, objective is to reach the specified money goal based off the rounds you chose.(The money goal = rounds x 10) ")
    print("Each round you will gets to choose 4 options, Loot, Steal, Job, Shop or XXX. Choosing any options except shop or XXX will pass a round.")
    print("(E.G. Round 1: User chooses Loot, game now moves on to round 2.)")
    print("4 Options:")
    print("Loot: gives you a chance to get a medium amount of money but also a chance to not get any money that round.")
    print("(Generate random, 80% chance to gain $10 and 20% chance to get nothing that round.)")
    print("Steal: gives you a chance to get a money but also a chance to lose money that round.")
    print("(50% chance to lose 30% of current balance or 50% chance to gain 40% of current balance)")
    print("Job: Nothing to lose but will get a math question like 2+2 to get a small amount of money if answered correctly.")
    print("($8 if you get question right and if wrong you will gain nothing during that round.)")
    print("Shop: You can access a shop which displays a menu of upgrades with costs.")
    print("Loot Upgrade: Increase reward from loot by $3 for $10")
    print("Steal Upgrade: Increase percentage to get money from steal by 10% for $15")
    print("Job Upgrade: Increase reward from job by $5 from jobs for $20)")
    print("When game ends you will gets asked if you want to play the game again.")
    return ""

def askNum(text):
    """Retunrs an integer from input using 'text'. Loops until valid input given."""
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Incorrect Input!")

def calc(a,ops,b):
    """Returns integer operation result from using : 'a','ops','b'"""
    if   ops == "+": return a+b
    elif ops == "-": return a-b
    elif ops == "*": return a*b

print("Welcome to the game Getting Lucky!")

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
    loot_up = 0
    job_up = 0
    while balance < goal:
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
            break

        if choice == "shop":
            print("Welcome to the store!")
            while True:
                print("Your current balance ${:.2f}".format(balance))
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
                            loot_up += 3
                        elif buy == "steal":
                            steal_up += 10
                        if buy == "job":
                            job_up += 5
            
                    elif balance < price:
                        print("You don't have enough money")
                        missing = balance - price
                        print("You are missing $", missing)

                else:
                    print("Please choose something from list")
        
        elif choice == "loot":
            chosen = random.choice(tokens)

                
            if chosen == "win":
                balance += win + loot_up
                print("You looted and found ${} \nbalance = ${:.2f}".format(win + loot_up, balance))
            
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
            nums = range(1,11)
            ops = random.choice("+-*")
            a,b = random.choices(nums, k=2)


            result = askNum("What is {} {} {} = ".format(a,ops,b))

            # calculate correct result
            answer = calc(a,ops,b)
            if  result == answer:
                balance += 8 + job_up
                rounds_played += 1
                print("Correct")
                print(balance)
            else:
                print("Wrong. Correct solution is: {} {} {} = {}".format(a,ops,b,answer))
                rounds_played += 1
                print(balance)
    if balance >= goal :
        print("Congratulations! You Won!")
    if play == True:
        again= yes_no("Do you want to play again, type yes or no ")
        if again == "no":
            play = False
print("Thank you for playing")