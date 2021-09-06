print("Welcome to the store!")
price_list = {'apple':3, 'orange':2, 'grapefruit':5, 'bomb':15, 'gun':10}
print("You can buy:")
for key in price_list:
    item = key
    price = price_list[key]
    print(item, price)
