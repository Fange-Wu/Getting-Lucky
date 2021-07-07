print("Welcome to the store!")
price_list = {'apple':3, 'orange':2, 'grapefruit':5, 'bomb':15, 'gun':10}
print("You can buy:")
for key in price_list:
    item = key
    price = price_list[key]
    print(item, price)

budget = 20
while budget > 0:
    buy = input("What do you want to buy?")
    price = price_list[buy] #You will get an error if you give it a key it doesn't have
    budget -= price
    print("You bought: ", buy)
    print("It costed: $", price)