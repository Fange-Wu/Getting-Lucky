import random

def question(text):
    """Retunrs an integer from input using 'text'. Loops until valid input given."""
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


    # make sure not to go below 0 for -
    while ops == "-" and a<b:
        a,b = random.choices(nums,k=2)

    # as a formatted text 
    result = question("What is {} {} {} = ".format(a,ops,b))

    # calculate correct result
    correct = calc(a,ops,b)
    if  result == corr:
        correct += 1
        print("Correct")
    else:
        print("Wrong. Correct solution is: {} {} {} = {}".format(a,ops,b,corr))