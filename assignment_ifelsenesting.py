name = input("Hello! What is your name? ")
print(f"Hello, {name}! Would you like to know your role in the society? \nHeavily basing on the stereotypes, unfortunately. Type: \n1 if Yes, \n2 if No:")
choice = float(input())

if choice == 1:
    print(f"Well then, {name}. How old are you? ")
    age = int(input())
    if age < 18:
        print("It seems that you are a part of minority! \nWhat is your biological sex, then? Type: \n 1 if Male, \n 2 if Female:")
        sex = int(input())
        if sex == 1:
            print("You are still a boy. It is your duty to enjoy your childhood \nand learn accordingly to become a gentleman in the near future.")
        elif sex == 2:
            print("You are still a girl. Enjoy your childhood, observe politeness \nand strive to be a good example.")
        else:
            print("It appears that you are neither. To all on their own, I guess. \nJust kidding! In the modern world, everyone is free to express who they are!")
    elif age >= 18:
        print("You are an adult! \nWhat is your biological sex, then? Type: \n 1 if Male, \n 2 if Female:")
        sex = int(input())
        if sex == 1:
            print("You are a Man! You must know how to handle responsibilities and yourself. \nKeep improving!")
        elif sex == 2:
            print("You are a Woman! I'm afraid you no longer have a room for improvement, \nbecause you are a perfection! You are the building block of society, really. ")
        else:
            print("It appears that you are neither. To all on their own, I guess. \nJust kidding! In the modern world, everyone is free to express who they are!")

elif choice == 2:
    print("Okay then. Why did you even run this code?")

else:
    print("How do you expect me to respond to that?")