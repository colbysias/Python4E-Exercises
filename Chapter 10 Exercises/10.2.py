"""Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

Sample Execution:

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

d = dict()
fname = input("Enter file name: ")
delim = ':'
l = list()

try:
    fhand = open(fname)
except:
    print("File cannot be opened: ", fname)
    exit()

for line in fhand:
    if line.startswith("From "):
        words = line.split()[5]
        hour = words.split(delim)[0]
        d[hour] = d.get(hour,0) + 1
l = list(d.items())
l.sort()
for key, val in l:
    print(key, val)