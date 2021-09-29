import random
# Functions go here
def check_rounds():
    # loop keeps asking the question + error until user inputs a whole number between 10-30
    while True:

        round_error = "Please type an integer that is between 10-30"

        try:
            response = int(input("How many rounds: "))
            # prints error message when user inputs an number thats not 10-30
            if response < 10 or response > 30:
                print(round_error)
                continue
        
        # If user inputs something else e.g. letter or 15.5 prints error as well
        except ValueError:
            print(round_error)
            continue
        
        return response

def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False 
    while not valid:
        try:
            # question
            response = int(input(question))

            # if the amount is too low or too high
            if low < response <= high:
                return response


            # output an error
            else:
                print(error)
        
        except ValueError:
            print(error)

def valid_checker(userchoice):
    #function checks for loot, steal, job, shop and xxx inputs
    valid = False
    while not valid:
        # turns the input into lowercase
        response = input(userchoice).lower()
        # if the input is not in the 5 options prints error and asks question again
        if response not in ('loot', 'steal', 'job', 'shop', 'xxx'):
            print("")
            print("ERROR Please choose Loot, Steal, Job, Shop or XXX to quit ")
        # if user chooses an option it prints the choice and returns it
        else:
            print("You chose {}".format(response))
            userchoice == response
            return response
            break

def yes_no(question):
    valid = False
    # Function checks for yes and no
    while not valid:
        #turns input into lowercase
        response = input(question).lower()
        # If yes returns yes + accepts input
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no returns no + accepts input
        elif response == "no" or response == "n":
            response = "no"
            return response

        # ask user to enter a valid answer
        else: 
            print("Please answer yes / no ")

def instructions() :
    print("**** How to Play ****")
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
    # input returns as an integar using 'text' and loops until valid input given
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Incorrect Input!")

def calc(a,ops,b):
    # returns an math equation based on the random operation by using 'a','ops','b'
    if   ops == "+": return a+b
    elif ops == "-": return a-b
    elif ops == "*": return a*b


print("Welcome to the game Getting Lucky!")

# Asks user if they have played before and if 'yes' program continues and if 'no' program displays instruction on game
# yes_no function checks for a valid input which are yes and no and keeps asking question if user inputs invalid input
show_instructions = yes_no("Have you played the game before? \n(Yes or No): ")
if show_instructions == "no":
    instructions()

# 'play' is the main routine / loop for the game
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

    # while balance < goal means the user hasnt met the money goal and so the game keeps running
    while balance < goal:
        # if the rounds_played (number of rounds user has played) becomes greater than the number of rounds chosen at the start the user loses
        if rounds_played >= rounds:
                print("")
                print("You Lost!\nYou didn't meet the money goal!")
                #breaks the loop and leads into asking if the user wants to play again
                break
        print()
        # this part is outputed every round. Displays the number of rounds out of rounds and the money goal and current balance
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        print("Money Goal: ${}".format(goal))
        print("Current Balance: ${:.2f}".format(balance))
        # choice asks user to choose the 5 options: loot, steal, job, shop or xxx
        # valid_checker function that checks for input is valid out of the 5 options mentioned above and if invalid displays message asking user choose input again
        choice = valid_checker("Please choose Loot, Steal, Job, Shop or XXX to quit ")
        
        # if choice = xxx breaks while loop and leads into asking user if play again
        if choice == "xxx":
            break
        
        #SHOP
        if choice == "shop":
            print()
            print("Welcome to the shop!")
            print()
            print("Upgrading Loot adds $3 to the reward \nUpgrading Job adds $5 to the reward\nUpgrading Steal increases chance to steal money by 10%")
            print("(Upgrades can be bought multiple times)")
            while True:
                print()
                print("Your current balance ${:.2f}".format(balance))
                price_list = {'loot':10, 'steal':15, 'job':20}
                for key in price_list:
                    item = key
                    price = price_list[key]
                    print("{} upgrade | cost: ${}".format(item, price))
                print("(Type 'exit' to exit the shop)")
                buy = input("What do you want to buy? ").lower()
                if buy == "exit":
                    break
                elif buy in price_list:
                    price = price_list[buy]
                    if balance >= price:
                        balance -= price
                        print("You Bought:",buy)
                    
                        if buy == "loot":
                            loot_up += 3
                        elif buy == "steal":
                            steal_up += 10
                        if buy == "job":
                            job_up += 5
                    #if the users balance is less 
                    elif balance < price:
                        print("You don't have enough money")
                        missing = balance - price
                        print("You are missing $", missing)
                # asks user again to choose something from the list if input is not in the list of items
                else:
                    print("Please choose something from list")
        
        #LOOT
        elif choice == "loot":
            # chooses randomly out of the variable tokens which is an array of 5 options
            chosen = random.choice(tokens)

            # if chosen is win, adds the looted money to the balance
            if chosen == "win":
                balance += win + loot_up
                # displays balance and the money gained from loot
                print("You looted and found ${} \nBalance = ${:.2f}".format(win + loot_up, balance))
            
            # if chosen is not win prints this
            else:
                print("You didn't find anything")
            # adds 1 round to the rounds_played
            rounds_played += 1

        #STEAL
        elif choice == "steal":
            # chooses random number from 1-100
            chosen_num = random.randint(1, 100)
            # if number between 1 and 50 the user gains money
            if 1 <= chosen_num <= 50 + steal_up :
                chosen = "You stole money..."
                # user gains 40% of current balance
                balance = 1.4 * balance
            # if number between 51 and 100 the user loses money
            elif 51 + steal_up <= chosen_num <= 100 :
                chosen = "You got caught..."
                #user loses 30% of current balance
                balance = 0.7 * balance
            # prints if they got caught or stole money
            print(chosen)
            print("Balance = ${:.2f}".format(balance))
            # adds 1 round played to rounds_played
            rounds_played += 1
    
        #JOB
        elif choice == "job":
            # var nums can only be numbers 1 - 11
            nums = range(1,11)
            # ops = random operations plus, minus or times
            ops = random.choice("+-*")
            # a and b are the 2 numbers chosen randomly from 1-11
            a,b = random.choices(nums, k=2)

            # asks the maths question in the format 'num' 'operation' 'num'        
            result = askNum("What is {} {} {} = ".format(a,ops,b))

            # calculates the correct result
            answer = calc(a,ops,b)
            # if answer correct user gains money 
            if  result == answer:
                balance += 8 + job_up
                rounds_played += 1
                print("Correct")
                print("Balance = ${}".format(balance))
            # if answer wrong displays correct answer
            else:
                print("Wrong. Correct solution is: {} {} {} = {}".format(a,ops,b,answer))
                rounds_played += 1
                print("Balance = ${}".format(balance))
    
    # if balance greater or equal to money goal user wins and leads into play again
    if balance >= goal :
        print("Congratulations! You Won!")
    # asks user if play again 
    if play == True:
        # yes_no function ensures user only inputs yes or no
        again= yes_no("Do you want to play again, type yes or no ")
        if again == "no":
            play = False
print("Thank you for playing")