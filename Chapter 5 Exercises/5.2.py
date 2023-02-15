#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

min = None
max = None


while True:
    line = input("Enter a number: ")
    try:
        fval = float(line)
        if max == None:
            max = fval
        elif max < fval:
            max = fval

        if min == None:
            min = fval
        elif min > fval:
            min = fval
    except:
        print("Invalid Input")
    if(line == 'done'):
        break


print("Maximum:", max, "Minimum:", min )
