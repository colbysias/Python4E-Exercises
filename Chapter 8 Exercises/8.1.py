#Exercise 1:

#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

#Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.



def chop(list):
    del list[0]
    del list[-1]
    return None

def middle(list):
    chop(list)
    print(list)

middle([1, 2, 3])
