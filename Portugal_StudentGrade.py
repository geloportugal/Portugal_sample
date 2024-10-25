print("Hello, student! Welcome to the GPA computer of LPU.")
name = input("What is your name?: ")
section = input ("What is your section?: ")
print("Please input your grades in:")

prelim = float(input("Prelim: "))
midterm = float(input("Midterm: "))
finals = float(input("Finals: "))


if prelim and midterm and finals >= 40 and prelim and midterm and finals <=100:
    prelim = prelim * 0.3333
    midterm = midterm * 0.3333
    finals = finals * 0.3333
            
    #Round off to 2 decimals
    prelim_r = round(prelim, 2)
    midterm_r = round(midterm, 2)
    finals_r = round(finals, 2)
    
    #Add prelim, midterm and finals grade
    grade = prelim_r + midterm_r + finals_r
    
    grade = round(grade)
    
    print(f"Your final grade: {grade}")
    
    if grade < 75:
        print(f"Hello, {name}! Your GPA is 5.00")
    elif grade >= 75 and grade <= 77:
        print(f"Hello, {name}! Your GPA is 3.00")
    elif grade >= 78 and grade <= 80:
        print(f"Hello, {name}! Your GPA is 2.75")
    elif grade >= 81 and grade <= 83:
        print(f"Hello, {name}! Your GPA is 2.50")
    elif grade >= 84 and grade <= 86:
        print(f"Hello, {name}! Your GPA is 2.25")
    elif grade >= 87 and grade <= 89:
        print(f"Hello, {name}! Your GPA is 2.00")
    elif grade >= 90 and grade <= 92:
        print(f"Hello, {name}! Your GPA is 1.75")
    elif grade >= 93 and grade <= 95:
        print(f"Hello, {name}! Your GPA is 1.50")
    elif grade >= 96 and grade <= 98:
        print(f"Hello, {name}! Your GPA is 1.25")
    elif grade >= 99 and grade <= 100:
        print(f"Hello, {name}! Your GPA is 1.00")
    
else:
    print("Please input a valid grade. \n1. Must be a number\n2. Must be greater than or equal to 40 and less than or equal to 100.")
    
