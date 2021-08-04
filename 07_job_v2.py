import random

def askNum(text):
    """Retunrs an integer from input using 'text'. Loops until valid input given."""
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Incorrect Input!")

def calc(a,ops,b):
    """Returns integer operation result from using : 'a','ops','b'"""
    if   ops == "+": return a+b
    elif ops == "-": return a-b
    elif ops == "*": return a*b


balance = 0
nums = range(1,11)
for i in range(0,10):
    ops = random.choice("+-*")
    a,b = random.choices(nums, b=2)


    result = askNum("What is {} {} {} = ".format(a,ops,b))

    # calculate correct result
    answer = calc(a,ops,b)
    if  result == answer:
        balance += 8
        print("Correct")
        print(balance)
    else:
        print("Wrong. Correct solution is: {} {} {} = {}".format(a,ops,b,answer))
        print(balance)

