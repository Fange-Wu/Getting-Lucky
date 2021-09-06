balance = 100
loot_up = 0
steal_up = 0
job_up = 0
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

print(loot_up, steal_up, job_up)

