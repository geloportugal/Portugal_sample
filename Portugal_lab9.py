row = int(input("Enter the number of rows: "))
num = 1

for x in range(1, row + 1):
    for y in range(x):
        print(num, end=" ")
        num += 1
    print('')