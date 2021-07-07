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


rounds_played = 0
rounds = check_rounds()
end_game = "no"
tokens = ["win", "win", "win", "win","lose"]
STARTING_BALANCE = 0
upgrade = 0
win = 8 + upgrade
balance = STARTING_BALANCE
balance = 100
while end_game == "no":
    
    # Rounds Heading
    print()
    heading = "Round {} of {}".format(rounds_played + 1, rounds)
    print(heading)
    choice = valid_checker("Please choose Loot, Steal, Job, Shop or XXX to quit ")

    if choice == "shop":
        print("Welcome to the store!")
        while True:
            
            print("1. Increase loot reward by $3 | cost: $10")
            print("2. Increase successful steal chance by 10% | cost: $15")
            print("3. Increase job reward to $10 | cost: $20")
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
                    print("Balance: $", balance)

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
    
    elif choice == "steal":
        chosen_num = random.randint(1, 100)
        if 1 <= chosen_num <= 50:
            chosen = "You stole money."
            balance = 1.3 * balance
        elif 51 <= chosen_num <= 100 :
            chosen = "You got caught."
            balance = 0.7 * balance
        print(chosen + "\nYour balance is ${:.2f} " .format(balance))

    elif choice == "job":
        operation = random.randint(1,3)
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)

        if operation == 1:
            question = int(input("What is " + str(num1) + "+" + str(num2) + ": "))
            answer = num1 + num2
            if question == answer:
                print("You got it right")
                balance += 6
            else:
                print("You got it wrong")

        elif operation == 2:
            question = int(input("What is " + str(num1) + "-" + str(num2) + ": "))
            answer = num1 - num2
            if question == answer:
                print("You got it right")
                balance += 6
            else:
                print("You got it wrong")

        elif operation == 3:
            question = int(input("What is " + str(num1) + "x" + str(num2) + ": "))
            answer = num1 * num2
            if question == answer:
                print("You got it right")
                balance += 6
            else:
                print("You got it wrong")
        
        print("balance = ${}".format(balance))


    rounds_played += 1

print("Thank you for playing")