# in python immutable meaning: it was pointing to location x, now if you change the value of it, it will point to location y

# e.g.
x = 10  # x -> 0x33
y = x   # y -> 0x33
x = 15  # x -> 0x443 but y is still pointing to 0x33

# same goes with string, if name = "ashish" has memory address 0x12
# and someone does name = "Abhay" now memory address will be 0x134 and the older will be cleaned by garbage collector

# we can verify this using id()
name = "Ashish"
id(name) # 4380083856
name = "Ashish Shah"
id(name) # 4380085488


# if we can change value of attribute in-place then it is mutable else it is not