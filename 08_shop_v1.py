

balance = 5
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
  

        elif balance < price:
            print("You don't have enough money")
            missing = balance - price
            print("You are missing $", missing)

    else:
        print("Please choose something from list")
    

