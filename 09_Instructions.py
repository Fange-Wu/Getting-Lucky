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

# Main Routine goes here...
def instructions () :
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

show_instructions = yes_no("Have you played the game before? ")

if show_instructions == "no":
    instructions()