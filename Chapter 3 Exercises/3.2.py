#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
#The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

try:
    hours = int(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
except:
    print("Error, please enter a numeric input")
overtimePay = 0

if hours > 40:
    overtimeHours = hours-40
    overtimePay = overtimeHours * 1.5 * rate


pay = hours * rate + overtimePay
print("Pay:", pay)
