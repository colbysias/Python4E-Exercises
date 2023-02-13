#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):

    overtimepay = 0

    if hours > 40:
        overtimeHours = hours-40
        overtimepay = overtimeHours * (1.5 * rate)


    pay = (hours - overtimeHours) * rate + overtimepay
    print("Pay:", pay)

num1 = int(input("Enter Hours:"))
num2 = int(input("Enter Rate:"))
computepay(num1, num2)