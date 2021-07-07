

balance = 15
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
    

print("You can buy:")
for key in price_list:
        item = key
        price = price_list[key]
        print("{} upgrade | cost: ${}".format(item, price))