import sys

my_list = [1, 2, 3] # 2 because when i'll call the function it will consider as one again pointing to this variable
your_list = my_list
hello_list = your_list
count = sys.getrefcount(my_list)
print(count)


# with numbers and string: garbage collection is done a bit of late because python thinks it might use it again