import random

for item in range (0,10) :
    operation = random.randint(1,3)
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    if operation == 1:
        question = int(input("What is " + str(num1) + "+" + str(num2) + ": "))
        answer = num1 + num2
        if question == answer:
            print("You got it right")
        else:
            print("You got it wrong")

    elif operation == 2:
        question = int(input("What is " + str(num1) + "-" + str(num2) + ": "))
        answer = num1 - num2
        if question == answer:
            print("You got it right")
        else:
            print("You got it wrong")

    elif operation == 3:
        question = int(input("What is " + str(num1) + "x" + str(num2) + ": "))
        answer = num1 * num2
        if question == answer:
            print("You got it right")
        else:
            print("You got it wrong")