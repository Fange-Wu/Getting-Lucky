import random

def question(text):
    
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Incorrect Input!")

def calc(a,ops,b):
    if   ops == "+": return a+b
    elif ops == "-": return a-b
    elif ops == "*": return a*b

nums = range(1,11)
for _ in range (0,10):
    ops = random.choice("+-*")
    a,b = random.choices(nums)


    # as a formatted text 
    result = question("What is {} {} {} = ".format(a,ops,b))

    # calculate correct result
    correct = calc(a,ops,b)
    if  result == correct:
        print("Correct")
    else:
        print("Wrong. The answer was: {} {} {} = {}".format(a,ops,b,correct))