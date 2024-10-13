grade = float(input("What is your grade? \n"))

if 0 <= grade <= 100:
    if grade < 74.5:
        print("Your Grade Point is 5.0")
    elif 74.5 <= grade < 77.5:
        print("Your Grade Point is 3.0")
    elif 77.5 <= grade < 80.5:
        print("Your Grade Point is 2.75")
    elif 80.5 <= grade < 83.5:
        print("Your Grade Point is 2.50")
    elif 83.5 <= grade < 86.5:
        print("Your Grade Point is 2.25")
    elif 86.5 <= grade < 89.5:
        print("Your Grade Point is 2.00")
    elif 89.5 <= grade < 92.5:
        print("Your Grade Point is 1.75")
    elif 92.5 <= grade < 95.5:
        print("Your Grade Point is 1.50")
    elif 95.5 <= grade < 98.5:
        print("Your Grade Point is 1.25")
    else:
        print("Your Grade Point is 1.00")

else:
    print("Please input a valid grade score.")