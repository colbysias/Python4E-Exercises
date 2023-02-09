#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
overtimePay = 0

if hours > 40:
    overtimeHours = hours-40
    overtimePay = overtimeHours * 1.5 * rate


pay = hours * rate + overtimePay
print("Pay:", pay)