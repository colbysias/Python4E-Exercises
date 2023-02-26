#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.
import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'
fname = input("Enter a file name: ")

d = dict()
l = list()


try:
    fhand = open(fname)
except:
    print("File cannot be opened", fname)
    exit()
text = fhand.read()

for ch in text:
    if ch in alphabet:
        d[ch] = d.get(ch,0) + 1
for key, val in d.items():
    l.append((val,key))
l.sort(reverse=True)
for key, val in l:
    print(key, val)






