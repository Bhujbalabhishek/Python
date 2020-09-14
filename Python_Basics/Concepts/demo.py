#difference between is and == operators

li1 = [1,2,3,4]
li2 = li1
li3 = list(li1) #lili2 pointing to different objects 

print(li1)
print(li2)
print(li3)

# The == operator is used when the values of two operands are equal, then the condition becomes true.
print(li1 == li2)
print(li1 == li3)

#The is operator evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
# as lili2 is pointing to different object thats why bhujju is lili2 is false  
print(li1 is li2)
print(li1 is li3)


# What is reference counting and how it defers from garbage collection?

ab = 7  #reference count for ab is 1 
xy = ab #reference count increases by 1 as xy is also refering to the same 7 value 

print(xy)
print(ab)


import sys
print(sys.getrefcount(xy)) # to count how many reference xy is having getrefcount method is used 

del ab

print(xy)

ab = 11
print(ab)


class MyClass(object):
    pass

a = MyClass()
a.obj = a
del a
# print(a)

# defined a new class and then created a new instance of class and assigned the instance to be property on itself 
# and then deleted the instance By deleting the instance, it’s no longer accessible in our Python program. However, Python didn’t destroy the instance from memory. The instance doesn’t have a reference count of zero because it has a reference to itself.
# it is called reference cycle 
# then we cannot use reference count we have to use garbage collection


import gc
print(gc.get_threshold())
print(gc.get_count())
