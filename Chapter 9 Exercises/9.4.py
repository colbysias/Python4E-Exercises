"""Exercise 4: Add code to the above program to figure out who has the most messages in the file.

After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Section [maximumloop]) to find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195"""

d = dict()
maxvalue = None
num = None
fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened: ", fname)
    exit()

for line in fhand:
    if line.startswith("From "):
        words = line.split()[1]
        d[words] = d.get(words,0) + 1

print(max(d, key=d.get), max(d.values()))
