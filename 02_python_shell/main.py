def say_name(name):
    print("Hey your name is", name, ", right?")

def print_age(age):
    print("Hey I know your age,", age)

def print_name_and_age(name, age):
    print("Hey your name is ", name, "and age is ", age)

name = "Ashish Shah"

# import main.py
# main.method(): to access methods
# main.variable: to access attributes
# but after updating in the code, I've to kill the terminal and import again but everything will be lost
# without importing again: i'll get attributeError: moduel 'main' has no attribute for fn as well
# to solve this, I can use hot reload module
age = 22
address = "BLR, Karnataka"


# to hot reload: use 
# from importlib import reload
# now you can reload the file: reload(filename)