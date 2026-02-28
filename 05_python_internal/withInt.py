a = 10
b = a 
a = 14 # b = 10 pointing to the same memory address

# pointing: a = b
# creating with same value a = [1, 2, 3] b = [1, 2, 3]
print(a == b) # True
print(a is b) # False because memory ref is not same

>>> l1 = [1, 2, 3, 4]
>>> l2 = l1
>>> l1
[1, 2, 3, 4]
>>> l2
[1, 2, 3, 4]
>>> l1 is l2
True
>>> l2 is l1
True
>>> l2 = [1, 2, 3]
>>> l2
[1, 2, 3]
>>> l2 is l1
False
>>> l1 is l2
False
>>> 