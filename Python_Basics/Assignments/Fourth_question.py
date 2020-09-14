# List Comprehension
#List comprehension is an elegant way to define and create lists based on existing lists.

# using for loop
# nums = []
# n =int(input("enter how many odd numbers you reqired in a list"))
#
#
# for i in range(n):
#     if i % 2 ==0:
#         pass
#     else:
#         nums.append(i)
# print(nums)

# using List comprehension
n =int(input("enter how many odd numbers you reqired in a list"))
only_odd = [num for num in range(1,n) if num%2==1 ]
print(only_odd)

