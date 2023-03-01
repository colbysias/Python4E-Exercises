"""Exercise 2: Write a program to look for lines of the form

`New Revision: 39772`
and extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259"""
import re
fname = input("Enter a file name: ")
fhand = open(fname)
sum = 0
count = 0

for line in fhand:
    line = line.rstrip()
    num = re.findall('^New Revision: ([0-9.]+)', line)
    for val in num:
        val = float(val)
        sum += val
        count += 1

print(sum / count)



