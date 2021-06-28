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

# Main routine goes here

rounds_played = 0
choose_instruction = "Please choose Loot, Steal, Job, Shop or XXX to quit"

rounds = check_rounds()

end_game = "no"
while end_game == "no":
    
    # Rounds Heading
    print()
    heading = "Round {} of {}".format(rounds_played + 1, rounds)
    print(heading)
    choose = input("{} or 'xxx to end: ".format(choose_instruction))    
    
    if choose == "xxx":
        break

    

    print("You chose {}".format(choose))

    rounds_played += 1

print("Thank you for playing")