print("Hello! Welcome to the LPU-Cavite Class Average Calculator.")


grades = []
studentnum = 1
while True:
    grade = input(f"Grade of student {studentnum}: ")
    if grade.isdigit():
        grade = int(grade)
        if grade >=40 and grade <= 100:
            grades.append(grade)    
        else:
            print("Please enter a valid grade.")
            break
        studentnum += 1
    elif grade == "done":
        sum(grades)
        avg = sum(grades)/len(grades)
        
        grade_ttl = 0
        passed = 0
        
        if grades != []:
            for grade in grades:
                grade_ttl += grade
                grade_ave = grade_ttl / len(grades)
            else:
                print(f"Average:  {grade_ave:.2f}")
            for grade in grades:
                if grade >= 75:
                    passed += 1
            else:
                print(f"Students passed: {passed}")
                passing_rate = (passed / len(grades))*100
                print(f"Passing Rate: {passing_rate:.2f}")
                break