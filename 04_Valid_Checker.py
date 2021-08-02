def valid_checker():
    while True:
        userchoice = input("Choose Loot, Steal, Job, Shop or XXX to quit ").lower()
        if userchoice.lower() not in ('loot', 'steal', 'job', 'shop', 'xxx'):
            print("ERROR Please choose Loot, Steal, Job, Shop or XXX to quit ")
        else:
            print("You chose {}".format(userchoice))
            break

while True :
    valid_checker()